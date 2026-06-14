#!/usr/bin/env python3
from pathlib import Path
import html
import re
import sqlite3
import subprocess
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / 'blog'
POSTS_DIR = BLOG_DIR / 'posts'
ASSETS_DIR = BLOG_DIR / 'assets' / 'uploads'
INDEX_PATH = ROOT / 'index.html'
CSS_PATH = ROOT / 'css' / 'main.css'

TITLE_TO_SLUG = {
    'We are a primitive people': 'we-are-a-primitive-people',
    'Build what it is you want to build': 'build-what-it-is-you-want-to-build',
    'Less noise texture mixin': 'less-noise-texture-mixin',
    'Twig.gr - How I learned to stop worrying and ship my side projects': 'twig-gr-how-i-learned-to-stop-worrying-and-ship-my-side-projects',
    'OAuth Consumer in CakePHP 2.0.5': 'oauth-consumer-in-cakephp-2-0-5',
    'Smarter images in Jadu CMS': 'smarter-images-in-jadu-cms',
    'Coursefinder 2010 report': 'coursefinder-2010-report',
    "Building a 'killer coursefinder'": 'building-a-killer-coursefinder',
    'Working to a structured development process': 'working-to-a-structured-development-process',
    'My year in moblogs': 'my-year-in-moblogs',
    'Playing with the Lumix LX3': 'playing-with-the-lumix-lx3',
    'Project52 fail': 'project52-fail',
    'An analogy for progressive enhancement': 'an-analogy-for-progressive-enhancement',
    'Quotes from Richard Branson': 'quotes-from-richard-branson',
    "You're missing the iPoint": 'youre-missing-the-ipoint',
    "Using PHP's alternate syntaxes": 'using-phps-alternate-syntaxes-to-aid-code-readability',
    'Redesigning Coffeepowered': 'redesign',
    'Nurturing my pet projects': 'nurturing-my-pet-projects',
    'CSS coding standards': 'css-coding-standards',
    'Encouraging impulse purchases': 'encouraging-impulse-purchases',
    'Quick and dirty dropdown pagination in CakePHP': 'quick-and-dirty-dropdown-pagination-in-cakephp',
    'The best quotes from FOWA': 'the-best-quotes-from-fowa',
    'Deliciously Timed Tweets': 'deliciously-timed-tweets',
    'Lose the snooze': 'lose-the-snooze',
    'New stylings': 'new-stylings',
    'Printable logos': 'printable-logos',
    'Featured : Designers scribbles': 'featured-designers-scribbles',
    'Meaningful milestones': 'meaningful-milestones',
    'Font sizes and accessibility': 'font-sizes-and-accessibility',
    'Contextual CSS': 'contextual-css',
    'Colouring in': 'colouring-in',
}

DEAD_LINK_FALLBACKS = {
    'https://www.ucisa.ac.uk/en/groups/cisg/Events/2010/cisg2010.aspx': 'https://web.archive.org/web/20100912164019/http://www.ucisa.ac.uk/en/groups/cisg/Events/2010/cisg2010.aspx',
    'http://www.online-information.co.uk/online2010/conference.html': 'https://web.archive.org/web/20100403035725/http://www.online-information.co.uk/online2010/conference.html',
}

DIRECT_LINK_REWRITES = {
    'http://www.themakersofthings.co.uk': 'https://themakersofthings.co.uk/model-engineer',
    'http://vimeo.com/62024423': 'https://themakersofthings.co.uk/model-engineer',
}

WP_UPLOAD_PREFIX = 'http://coffeepowered.co.uk/wp-content/uploads/'
USER_AGENT = 'Mozilla/5.0'


def slugify(title: str) -> str:
    return TITLE_TO_SLUG.get(title) or re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


def latest_ghost_commit() -> str:
    out = subprocess.check_output(
        ['git', 'log', '--format=%H', '--diff-filter=A', '--', 'content/data/ghost.db'],
        cwd=ROOT,
        text=True
    )
    return out.splitlines()[-1].strip()


def export_ghost_db(commit: str) -> Path:
    tmp = Path(tempfile.gettempdir()) / 'coffeepowered-ghost.db'
    with tmp.open('wb') as f:
        subprocess.run(['git', 'show', f'{commit}:content/data/ghost.db'], cwd=ROOT, check=True, stdout=f)
    return tmp


def fetch_rows(db_path: Path):
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "select title,slug,markdown,html,meta_description,published_at,image from posts where status='published' and page=0 order by published_at desc"
    ).fetchall()
    conn.close()
    return rows


def date_from_ms(ms: int) -> str:
    dt = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
    return dt.strftime('%Y-%m-%d')


def display_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return dt.strftime('%Y - %b %d')


def text_content(source: str) -> str:
    text = re.sub(r'<[^>]+>', ' ', source or '')
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def excerpt_text(source: str, limit: int = 180) -> str:
    cleaned = text_content(source)
    cleaned = re.sub(r'https?://\S+', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned[:limit].rstrip() + ('...' if len(cleaned) > limit else '')


def wayback_asset_url(url: str) -> str:
    return f'https://web.archive.org/web/0im_/{url}'


def local_asset_url(url: str) -> str:
    rel = url.replace(WP_UPLOAD_PREFIX, '')
    dest = ASSETS_DIR / rel
    if dest.exists() and dest.stat().st_size > 0:
        return '/blog/assets/uploads/' + rel
    return ''


def build_local_map(rows):
    m = {}
    for row in rows:
        slug = slugify(row['title'])
        year, month, _ = date_from_ms(row['published_at']).split('-')
        m[f'http://coffeepowered.co.uk/{year}/{month}/{row["slug"]}/'] = f'/blog/posts/{year}/{month}/{slug}/'
    return m


def rewrite_html(content: str, local_map: dict) -> str:
    if not content:
        return ''
    out = content.replace('src="http://player.vimeo.com/', 'src="https://player.vimeo.com/')
    out = out.replace('<p><div class="codecolorer-container', '<div class="codecolorer-container')
    out = out.replace('</div></p>', '</div>')
    out = out.replace('<p><div class="wp-caption', '<div class="wp-caption')
    out = out.replace('”', '&rdquo;').replace('“', '&ldquo;')

    def repl_href(match):
        attr, url = match.group(1), match.group(2)
        new = url
        if url in local_map:
            new = local_map[url]
        elif url in DIRECT_LINK_REWRITES:
            new = DIRECT_LINK_REWRITES[url]
        elif url in DEAD_LINK_FALLBACKS:
            new = DEAD_LINK_FALLBACKS[url]
        elif url.startswith(WP_UPLOAD_PREFIX):
            new = local_asset_url(url) or wayback_asset_url(url)
        return f'{attr}="{html.escape(new, quote=True)}"'

    out = re.sub(r'(href|src)="([^"]+)"', repl_href, out)
    out = normalize_code_blocks(out)
    return out


def normalize_code_blocks(content: str) -> str:
    def repl(match):
        block = match.group(0)
        container_match = re.search(r'<div class="([^"]*codecolorer-container[^"]*)"', block, flags=re.S)
        language = prism_language(container_match.group(1) if container_match else '')
        code_match = re.search(
            r'<div class="(?=[^"]*\bcodecolorer\b)(?![^"]*codecolorer-container)[^"]*"[^>]*>(.*?)</div>\s*</td>\s*</tr>\s*</tbody>\s*</table>',
            block,
            flags=re.S,
        )
        if not code_match:
            return block
        code_html = code_match.group(1)
        code_html = re.sub(r'<br\s*/?>', '\n', code_html, flags=re.I)
        code_html = re.sub(r'</p>\s*<p[^>]*>', '\n\n', code_html, flags=re.I)
        code_html = re.sub(r'<p[^>]*>', '', code_html, flags=re.I)
        code_html = re.sub(r'</p>', '', code_html, flags=re.I)
        code_text = re.sub(r'<[^>]+>', '', code_html)
        code_text = html.unescape(code_text).replace('\xa0', ' ')
        code_text = re.sub(r'\n{3,}', '\n\n', code_text)
        code_text = '\n'.join(line.rstrip() for line in code_text.splitlines()).strip('\n')
        if not code_text.strip():
            return block
        return f'<pre class="blog-code line-numbers language-{language}"><code class="language-{language}">{html.escape(code_text)}</code></pre>'

    out = re.sub(
        r'<div class="codecolorer-container[^"]*"[^>]*>.*?</table>\s*</div>',
        repl,
        content,
        flags=re.S,
    )
    out = re.sub(r'</pre>\s*###\s*(.*?)</p>', r'</pre><h3>\1</h3>', out, flags=re.S)
    out = re.sub(r'</pre>\s*([^<\n][^<]*?)</p>', r'</pre><p>\1</p>', out, flags=re.S)
    return out


def prism_language(class_names: str) -> str:
    tokens = set(class_names.split())
    if 'php' in tokens:
        return 'php'
    if 'css' in tokens or 'less' in tokens:
        return 'css'
    if 'javascript' in tokens or 'js' in tokens:
        return 'javascript'
    if 'html' in tokens or 'markup' in tokens or 'xml' in tokens:
        return 'markup'
    return 'none'


def blog_shell(title: str, description: str, inner: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} | Coffeepowered</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="icon" type="image/svg+xml" href="/img/favicon.svg?v=20260419-2">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/main.css?v=20260419-2">
    <link rel="stylesheet" type="text/css" href="/vendor/font-awesome/css/font-awesome.min.css?v=20260419-2">
    <link rel="stylesheet" type="text/css" href="/vendor/prism/prism.css">
    <link rel="stylesheet" type="text/css" href="/vendor/prism/prism-line-numbers.min.css">
    <script defer src="/vendor/prism/prism.js"></script>
    <script defer src="/vendor/prism/prism-markup.min.js"></script>
    <script defer src="/vendor/prism/prism-clike.min.js"></script>
    <script defer src="/vendor/prism/prism-css.min.js"></script>
    <script defer src="/vendor/prism/prism-javascript.min.js"></script>
    <script defer src="/vendor/prism/prism-php.min.js"></script>
    <script defer src="/vendor/prism/prism-line-numbers.min.js"></script>
</head>
<body>
    <main class="page page-blog" id="top">
        <header class="top-nav">
            <a class="brand" href="/">Coffeepowered</a>
            <nav class="top-nav-links" aria-label="Primary">
                <a href="/">Home</a>
                <a href="/blog/">Archive</a>
            </nav>
        </header>
        {inner}
    </main>
</body>
</html>
'''


def sidebar_html(current_title: str, posts):
    items = []
    for post in posts:
        href = post['href']
        current = ' aria-current="page"' if post['title'] == current_title else ''
        current_class = ' is-current' if post['title'] == current_title else ''
        items.append(
            f'<li><a class="blog-sidebar-link{current_class}" href="{href}"{current}>'
            f'<span class="blog-sidebar-date">{post["date"]}</span>'
            f'<span class="blog-sidebar-title">{html.escape(post["title"])}</span>'
            f'</a></li>'
        )
    return f'''
        <aside class="blog-sidebar">
            <section class="blog-sidebar-panel blog-profile-card" aria-label="Profile">
                <figure class="blog-profile-media">
                    <img src="/img/stanton.png" alt="Paul Stanton headshot">
                </figure>
                <div class="blog-profile-copy">
                    <p class="blog-kicker">Paul Stanton</p>
                    <h2>AI / Platform / UX</h2>
                    <p>I build confidence, explainability, and sustainable scale across products and organisations.</p>
                    <div class="blog-profile-actions">
                        <a class="btn btn-primary" href="https://www.linkedin.com/in/paulstanton/">LinkedIn</a>
                        <a class="btn" href="mailto:paul@coffeepowered.co.uk">Email</a>
                    </div>
                </div>
            </section>
            <section class="blog-sidebar-panel" aria-label="Other archive posts">
                <p class="blog-kicker">Other Posts</p>
                <ol class="blog-sidebar-list">{''.join(items)}</ol>
            </section>
        </aside>
    '''


def post_page(post, posts):
    prev_html = ''
    next_html = ''
    idx = next(i for i, p in enumerate(posts) if p['title'] == post['title'])
    if idx > 0:
        prev = posts[idx - 1]
        prev_html = f'<a class="blog-adjacent prev" href="{prev["href"]}"><span class="blog-adjacent-label">Newer Post</span><span class="blog-adjacent-title">{html.escape(prev["title"])}</span></a>'
    if idx < len(posts) - 1:
        nxt = posts[idx + 1]
        next_html = f'<a class="blog-adjacent next" href="{nxt["href"]}"><span class="blog-adjacent-label">Older Post</span><span class="blog-adjacent-title">{html.escape(nxt["title"])}</span></a>'
    body = f'''
        <div class="blog-post-layout">
            <article class="blog-post blog-post-main blog-post-{post['slug']}">
                <h1>{html.escape(post['title'])}</h1>
                <p class="blog-meta">{post['date']}</p>
                <div class="blog-note"><p>This post has been restored from the original Coffeepowered archive. Content is preserved, but legacy layout, embeds, and media may not match the original presentation exactly.</p></div>
                <div class="blog-body">{post['body']}</div>
                <footer class="blog-footer">
                    <div class="blog-actions">
                        <p><a href="{html.escape(post['source'])}"><i class="fa fa-link" aria-hidden="true"></i> Source capture</a></p>
                        <p><a href="/blog/"><i class="fa fa-arrow-left" aria-hidden="true"></i> Back to archive</a></p>
                    </div>
                    <nav class="blog-pager" aria-label="Archive post navigation">{prev_html}{next_html}</nav>
                </footer>
            </article>
            {sidebar_html(post['title'], posts)}
        </div>
    '''
    return blog_shell(post['title'], post['description'], body)


def index_page(posts):
    cards = []
    for post in posts:
        cards.append(f'''<article class="writing-block archive-block">
                    <a class="archive-card-link" href="{post['href']}" aria-label="Open local archive post for {html.escape(post['title'])}">
                        <h3>{html.escape(post['title'])}</h3>
                        <p class="archive-meta">{display_date(post['date'])}</p>
                        <p>{html.escape(post['excerpt'])}</p>
                        <p class="archive-card-cta"><i class="fa fa-link" aria-hidden="true"></i> Read the post</p>
                    </a>
                </article>''')
    body = f'''
        <section class="panel spread blog-index">
            <h1>Writing Archive</h1>
            <div class="blog-note"><p>These posts have been restored into the current site. Content has been preserved where possible, but legacy layout, embeds, comments, and media treatment may differ from the original site.</p></div>
            <div class="blog-summary">
                <article><p class="fact-label">Posts</p><p class="fact-value">{len(posts)}</p></article>
                <article><p class="fact-label">Range</p><p class="fact-value">2008-2013</p></article>
                <article><p class="fact-label">Source</p><p class="fact-value">Ghost DB</p></article>
            </div>
            <div class="writing-spread archive-spread">{''.join(cards)}</div>
        </section>
    '''
    return blog_shell('Coffeepowered Archive', 'Recovered Coffeepowered writing archive from 2008 to 2013.', body)


def replace_homepage_archive(posts):
    html_text = INDEX_PATH.read_text()
    start = html_text.index('<h3 class="writing-subhead">Coffeepowered Archive</h3>')
    note_start = html_text.index('<p class="section-note"><a href="/blog/" aria-label="Browse the full Coffeepowered archive">Browse the full Coffeepowered archive</a></p>', start)
    contact = html_text.index('</section>\n\n                <section class="panel connect"', note_start)
    replacement = '<h3 class="writing-subhead">Coffeepowered Archive</h3>\n                    <p class="section-note"><a href="/blog/" aria-label="Browse the full Coffeepowered archive">Browse the full Coffeepowered archive</a></p>\n'
    new = html_text[:start] + replacement + html_text[contact:]
    INDEX_PATH.write_text(new)


def main():
    commit = latest_ghost_commit()
    db_path = export_ghost_db(commit)
    rows = fetch_rows(db_path)
    local_map = build_local_map(rows)
    posts = []
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    for row in rows:
        title = row['title']
        date = date_from_ms(row['published_at'])
        year, month, _ = date.split('-')
        slug = slugify(title)
        href = f'/blog/posts/{year}/{month}/{slug}/'
        body = rewrite_html(row['html'] or '', local_map)
        excerpt = excerpt_text(row['html'] or row['markdown'] or '', 180)
        description = row['meta_description'] or excerpt_text(row['html'] or row['markdown'] or '', 155)
        source = f'https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/{year}/{month}/{row["slug"]}/'
        posts.append({'title': title, 'date': date, 'slug': slug, 'href': href, 'body': body, 'excerpt': excerpt, 'description': description, 'source': source})
    for post in posts:
        out_dir = POSTS_DIR / post['date'][:4] / post['date'][5:7] / post['slug']
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / 'index.html').write_text(post_page(post, posts))
    (BLOG_DIR / 'index.html').write_text(index_page(posts))
    replace_homepage_archive(posts)
    print(f'Generated {len(posts)} posts from Ghost commit {commit}.')

if __name__ == '__main__':
    main()

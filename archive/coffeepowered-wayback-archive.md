# Coffeepowered Wayback Archive

Recovered from the Internet Archive Wayback Machine. Some captures contain spam injection in surrounding page chrome; post bodies were cleaned to remove that material.


## We are a primitive people

- Date: 2013-08-01

- Wayback URL: https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/2013/08/we_are_a_primitive_people/

- Status: ok


A quote from famed industrial designer Walter Dorwin Teague in the thirties seems to echo the current state of web design and development, namely a dramatic simplification of the predominant design style (dare I mention the F word?) coupled with, and possibly caused by, an explosion of new design techniques and tools that we’re racing to catch up with.

>

Walter Dorwin Teague“We achieve a high degree of simplicity because we are a primitive people, we have reverted again to a primitive state of human development. We are primitives in this new machine age. We have no developed history behind us to use in our artistic creations. We have no theories, no vocabulary of ornament, behind us to use in our work. That is why so much of our modern work today has a certain stark and simple quality that relates it very closely to the primitive work of Greece and the primitive work of Egypt and the primitive work of most people who were discovering their techniques and their tools.”

Walter Dorwin Teague, 1939


## Build what it is you want to build

- Date: 2013-06-24

- Wayback URL: https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/2013/06/build-what-it-is-you-want-to-build-and-learn-as-you-go/

- Status: ok


Some wise words in a nice little video series (https://web.archive.org/web/20140713204403/http://www.themakersofthings.co.uk/) I stumbled across today, a particularly hard punch when he goes on to say “…and don’t go back and rebuild or you’ll never get the thing finished” as I’m tinkering with rebuilding an existing site using Backbone.js to learn the language, I may never push the backbone version live but I’ve found it useful to work with a familiar set of data rather than start completely from scratch… or am I just kidding myself.

The Makers of Things: The Model Engineer (https://web.archive.org/web/20140713204403/http://vimeo.com/62024423) from Anne Holiday (https://web.archive.org/web/20140713204403/http://vimeo.com/theenglishholidayclub) on Vimeo (https://web.archive.org/web/20140713204403/http://vimeo.com/).

I’m looking for more videos like this, small documentary style films about people who make things. I love the Made By Hand series (https://web.archive.org/web/20140713204403/http://thisismadebyhand.com/) and the Knife Maker is one of my favourite things ever, focusing on the human side of craft and the desire to make the next thing you make the best version of it you’ve ever made. I can relate to that.

Made by Hand / No 2 The Knife Maker (https://web.archive.org/web/20140713204403/http://vimeo.com/31455885) from Made by Hand (https://web.archive.org/web/20140713204403/http://vimeo.com/madebyhand) on Vimeo (https://web.archive.org/web/20140713204403/http://vimeo.com/).

If you know more videos/series like this, please let me know!


## Less noise texture mixin

- Date: 2012-11-02

- Wayback URL: https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/2012/11/less-noise-texture-mixin/

- Status: ok


If you’d like to add a little bit of texture to your designs adding a subtle amount of noise can work wonders. By using a repeated monochrome noise png as a background image you can add noise to any element no matter what colour by using opacity to blend it in.

The mixin below uses a base64 encoded version in the stylesheet which means you don’t have to worry about including the file on your server, the one trade-off to consider is that the base64 encoded image data weighs in at 2kb and the binary .png version is 1.5kb. I personally prefer the cleanliness of having the mixin self-contained, but each to their own.

### The Mixin

We use a parametric mixin which has a sensible default opacity which you can change to suit your design and overridden when you need.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
/**

 * Adds a transparent noise texture as a background image to a given element.

 * Texture strength can be controlled with @opacity parameter.

 * By Paul Stanton (www.coffeepowered.co.uk)

 */

.noise (@opacity: .3) {

  &:before {

  bottom: 0;

  content: "";

  left: 0;

  opacity: @opacity;

  position: absolute;

  right: 0;

  top: 0;

  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAAUVBMVEWFhYWDg4N3d3dtbW17e3t1dXWBgYGHh4d5eXlzc3OLi4ubm5uVlZWPj4+NjY19fX2JiYl/f39ra2uRkZGZmZlpaWmXl5dvb29xcXGTk5NnZ2c8TV1mAAAAG3RSTlNAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEAvEOwtAAAFVklEQVR4XpWWB67c2BUFb3g557T/hRo9/WUMZHlgr4Bg8Z4qQgQJlHI4A8SzFVrapvmTF9O7dmYRFZ60YiBhJRCgh1FYhiLAmdvX0CzTOpNE77ME0Zty/nWWzchDtiqrmQDeuv3powQ5ta2eN0FY0InkqDD73lT9c9lEzwUNqgFHs9VQce3TVClFCQrSTfOiYkVJQBmpbq2L6iZavPnAPcoU0dSw0SUTqz/GtrGuXfbyyBniKykOWQWGqwwMA7QiYAxi+IlPdqo+hYHnUt5ZPfnsHJyNiDtnpJyayNBkF6cWoYGAMY92U2hXHF/C1M8uP/ZtYdiuj26UdAdQQSXQErwSOMzt/XWRWAz5GuSBIkwG1H3FabJ2OsUOUhGC6tK4EMtJO0ttC6IBD3kM0ve0tJwMdSfjZo+EEISaeTr9P3wYrGjXqyC1krcKdhMpxEnt5JetoulscpyzhXN5FRpuPHvbeQaKxFAEB6EN+cYN6xD7RYGpXpNndMmZgM5Dcs3YSNFDHUo2LGfZuukSWyUYirJAdYbF3MfqEKmjM+I2EfhA94iG3L7uKrR+GdWD73ydlIB+6hgref1QTlmgmbM3/LeX5GI1Ux1RWpgxpLuZ2+I+IjzZ8wqE4nilvQdkUdfhzI5QDWy+kw5Wgg2pGpeEVeCCA7b85BO3F9DzxB3cdqvBzWcmzbyMiqhzuYqtHRVG2y4x+KOlnyqla8AoWWpuBoYRxzXrfKuILl6SfiWCbjxoZJUaCBj1CjH7GIaDbc9kqBY3W/Rgjda1iqQcOJu2WW+76pZC9QG7M00dffe9hNnseupFL53r8F7YHSwJWUKP2q+k7RdsxyOB11n0xtOvnW4irMMFNV4H0uqwS5ExsmP9AxbDTc9JwgneAT5vTiUSm1E7BSflSt3bfa1tv8Di3R8n3Af7MNWzs49hmauE2wP+ttrq+AsWpFG2awvsuOqbipWHgtuvuaAE+A1Z/7gC9hesnr+7wqCwG8c5yAg3AL1fm8T9AZtp/bbJGwl1pNrE7RuOX7PeMRUERVaPpEs+yqeoSmuOlokqw49pgomjLeh7icHNlG19yjs6XXOMedYm5xH2YxpV2tc0Ro2jJfxC50ApuxGob7lMsxfTbeUv07TyYxpeLucEH1gNd4IKH2LAg5TdVhlCafZvpskfncCfx8pOhJzd76bJWeYFnFciwcYfubRc12Ip/ppIhA1/mSZ/RxjFDrJC5xifFjJpY2Xl5zXdguFqYyTR1zSp1Y9p+tktDYYSNflcxI0iyO4TPBdlRcpeqjK/piF5bklq77VSEaA+z8qmJTFzIWiitbnzR794USKBUaT0NTEsVjZqLaFVqJoPN9ODG70IPbfBHKK+/q/AWR0tJzYHRULOa4MP+W/HfGadZUbfw177G7j/OGbIs8TahLyynl4X4RinF793Oz+BU0saXtUHrVBFT/DnA3ctNPoGbs4hRIjTok8i+algT1lTHi4SxFvONKNrgQFAq2/gFnWMXgwffgYMJpiKYkmW3tTg3ZQ9Jq+f8XN+A5eeUKHWvJWJ2sgJ1Sop+wwhqFVijqWaJhwtD8MNlSBeWNNWTa5Z5kPZw5+LbVT99wqTdx29lMUH4OIG/D86ruKEauBjvH5xy6um/Sfj7ei6UUVk4AIl3MyD4MSSTOFgSwsH/QJWaQ5as7ZcmgBZkzjjU1UrQ74ci1gWBCSGHtuV1H2mhSnO3Wp/3fEV5a+4wz//6qy8JxjZsmxxy5+4w9CDNJY09T072iKG0EnOS0arEYgXqYnXcYHwjTtUNAcMelOd4xpkoqiTYICWFq0JSiPfPDQdnt+4/wuqcXY47QILbgAAAABJRU5ErkJggg==);

  }

}

### Usage

To apply noise to your element, just invoke the mixin!
1
2
3
4
.my-element {

  position: relative;

  .noise();

}

And override the opacity value if you wish
1
2
3
4
.my-element {

  position: relative;

  .noise(.5);

}

Here’s an example of two elements, one without and one with noise. It’s subtle, but that’s what I need for my projects, you could use a noise image with a higher contrast if you wish.

Thats it! If you use it, drop me a line!


## Twig.gr – How I learned to stop worrying and ship my side projects

- Date: 2012-02-06

- Wayback URL: https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/2012/02/twig-gr-how-i-learned-to-stop-worrying-and-ship-my-side-projects/

- Status: ok


I love to mess about with side projects, although I have a very bad habit which I think may be common amongst us in that I have so little free time to spend on the projects that it takes me so long to design and develop them, that I usually end up abandoning them at various stages while promising myself that I’ll come back to it later and finish it off, or I have (imho) great ideas that I never even start working on because I think I don’t have the time but after reading the Steve Jobs biography I had his mantra running around my head for a while.

>

Real artists ship.

Steve Jobs

It doesn’t matter how long you’ve spent working on something, or how clever you’ve been with the design or development if it’s sitting on a folder on your computer rather than in the hands of real people. I swore to myself that the next idea I had for a side project, I’d actually get off my ass and do it, however long it took with the little spare time I have, and I’d get it shipped as quickly as possible. (Shipping an imperfect, unfinished product isn’t quite what Steve meant, but hey…)

### The idea

Every now and again on my Twitter stream, one of the people I follow gets a games console and their friends reply back with their gamer handles so that they can connect on these systems and perhaps play online. I also send out my XBox Live gamertag every now and then to see if any of the people I follow also play the same kind of games as me so that if we’re ever online at the same time, I can jump into a game with them and play with some familiar faces. It gets wearing to constantly ask your twitter followers for their handles, so I figured I could build something to do this for us.

>

Idea for a side project, Twitter app where you add your Xbox/PS3/PC gamer ID’s and see the ID’s of the people you follow.

— Stanton (@stanton) January 6, 2012 (https://web.archive.org/web/20140713204358/https://twitter.com/stanton/status/155199096804741120)

After sending this tweet I had quite a few replies from interested parties, so as Richard Branson would say, I thought ‘Screw it, Let’s do it” and got to work. Knowing that my time was limited I decided to develop this rapidly, to a minimum feature set, and with little to no design work more than a basic wireframe. The idea was to get it in people’s hands as quickly as possible; If it takes off I’ll devote more time to it, if not then I’ve not wasted months of work.

### Minimum Viable Product

- User Add/Edit/Sign in

- Twitter oAuth

- XBL & PSN handles

- Add/Remove handles

- List handles of Twitter friends

- Ask user to post link to their friends

Twig.gr screenshot (https://web.archive.org/web/20140713204358/http://coffeepowered.co.uk/wp-content/uploads/2012/02/250px_1327962302_photo.jpg)

After scribbling down the ‘Minimum Viable Product’ feature set, I grabbed the latest version of CakePHP (https://web.archive.org/web/20140713204358/http://cakephp.org/) and 320 and up (https://web.archive.org/web/20140713204358/http://stuffandnonsense.co.uk/projects/320andup/) and got to work integrating with Twitter, I had to modify the OAuth Consumer component (https://web.archive.org/web/20140713204358/http://coffeepowered.co.uk/2012/01/oauth-consumer-in-cakephp-2-0-5/) for the latest version of Cake, but with the magic of GitHub I was able to push these changes back to the original author to be integrated into future versions. Within a few days I had a working prototype which I took to the New Adventures conference to get some feedback on while chatting with people at at the pre-party.

One of the hardest things was making the conscious effort not to spend too much time on the design, It’s ingrained in our industry and culture to put the design of a new product under the microscope and make snap judgements on the quality of a service based on it’s pixels but with the constraints I’d placed upon the project, design would have to come later so I threw some very simple colour and layout over the top to at least make it palatable for the users. and after a few evenings of steady coding I checked out the code onto the production server and threw the link onto Twitter.

### twig.gr

So twig.gr went live, and now we play the waiting game and to see how it goes, I’m quite happy for it to grow slowly and organically especially since I don’t have the means to conduct any kind of social media/marketing campaign for it, I think it’s one of those kinds of products that works truly by word of mouth. If you add yourself, you’re likely to tell others to sign up so that you can find them also. If it grows in popularity then I’ll devote more time to it both from a feature and design point of view, if not, then at least I shipped!


## OAuth Consumer in CakePHP 2.0.5

- Date: 2012-01-09

- Wayback URL: https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/2012/01/oauth-consumer-in-cakephp-2-0-5/

- Status: ok


Just a quick post to note some tweaks I had to make to Daniel Hofstetter’s awesome OAuth consumer component for CakePHP (https://web.archive.org/web/20140713202642/http://code.42dh.com/oauth/) to get it running in CakePHP 2.0.5

The cakephp_2.0-dev branch was throwing the following error for me when trying to use the Twitter OAuth API.
1
Consumer twitter_consumer.php not found!

The relevant changes are available in my cakephp_2.0.5 branch on Github (https://web.archive.org/web/20140713202642/https://github.com/Stanton/oauth-consumer-component/tree/cakephp_2.0.5).

### Changelog

- Rename directories to match new conventions.

- Change createConsumer method to use $className rather than $fileName to fix ‘Consumer twitter_consumer.php not found!’ exception.

- Use App::uses instead of App::import to fix ‘Fatal error: Class ‘HttpSocket’ not found…’ error.

### Get the code

https://github.com/Stanton/oauth-consumer-component/tree/cakephp_2.0.5


## Smarter images in Jadu CMS

- Date: 2011-09-02

- Wayback URL: https://web.archive.org/web/20140713224505/http://coffeepowered.co.uk/2011/09/smarter-images-in-jadu-cms/

- Status: ok


I’ve recently been looking at ways to enhance certain content types that we deliver through Jadu CMS (https://web.archive.org/web/20140713204354/http://jadu.net/), my focus at the moment has been through the use of images within content, whether that be News, Events, Documents or Homepages. This started with a re-alignment of the news section on the University of Leeds’ corporate website (https://web.archive.org/web/20140713204354/http://www.leeds.ac.uk/).

### Multiple image sizes

We’ve traditionally been hampered by the fact that Jadu doesn’t yet have the ability to generate multiple image sizes from a single base image so if I wanted to have a large document level image, and a smaller thumbnail within a list view, I’d either have to resize with CSS which results in degraded image quality in some browsers, or have the editors upload multiple versions of each image to the CMS and figure some way to switch between these programatically. Neither of these options were desirable, so we built an image helper that, instead of inserting the  element directly into the front end script, we pass the image name to the helper, along with the desired attributes such as a specific height and/or width, the helper then resizes the native image, and caches it for future use.
1
2
3
4
5
6
print imageGenerator($imageURL, array(

    'alt' => getImageProperty($imageURL, 'altText'),

    'class' => 'contentimage',

    'width' => 340

    )

);

Take the UoL Press Releases news section (https://web.archive.org/web/20140713204354/http://www.leeds.ac.uk/news/30292/press_releases), for example, we can now elegantly deliver multiple image sizes depending on our needs, without either the bandwidth overhead of resizing large images, or the administration headache of managing multiple images within the CMS, and the image helper can be used anywhere in our front end templates.

>

we can now elegantly deliver multiple image sizes depending on our needs, without either the bandwidth overhead of resizing large images, or the administration headache of managing multiple images within the CMS

### Image attribution

The next issue I’ve been looking into recently is that of image attribution, again, Jadu doesn’t currently have any options within the multimedia gallery module to attach attribution data to multimedia items. If the UoL wants to use a Creative Commons licensed image, there’s no way, other than adding the attribution data into the body content. I figured there was a better way to do this.

The Multimedia Module within Jadu is the central place to manage all types of multimedia content, for this example I’ll focus on images. One of the core concepts of a CMS is that an image only needs to exist once, but can then be included in any other piece of content. The multimedia manager is a relatively recent addition to Jadu CMS, and as such, provides the bare minimum of features required so I needed to find a way to link attribution data to an image without modifying the core CMS code.

### Enter machine tags

As we can apply tags to each image, this was a perfect place to use machine tags – a piece of text which contains machine-readable semantic information – to include the relevant licensing information. Machine tags are composed of three parts; a namespace, a predicate, and a value. For example:
1
2
3
license:creativecommons="© 2009 Greg Grossmeier, used under a Creative

Commons Attribution-ShareAlike license:

http://creativecommons.org/licenses/by-sa/3.0/"

Initially, I hit a brick wall in that the ‘tag’ column within the JaduMultimediaTags table was limited to varchar(50), a sensible default for most english word based tags but kills the chance of using machine tags which are typically longer. Frustrated, I moaned a bit on Twitter (https://web.archive.org/web/20140713204354/http://twitter.com/#!/stanton/status/108904319063048193), and within minutes had an email from @ap49 (https://web.archive.org/web/20140713204354/http://twitter.com/ap49) at Jadu asking what they could do to help, and later that night they’d modified the Jadu trunk to change the tag column to varchar(255) which is much more useful, for me at least!

So, armed with our enlarged tag column, I set about writing a function which would parse an images’ tags for our license machine tag, extract the relevant components, and spit out some meaningful markup to the browser which we could style as needed. You can get the Image License function from GitHub (https://web.archive.org/web/20140713204354/https://gist.github.com/599db38634c9ba2418d0), in case it’s of use to anyone.

For the University of Leeds’ corporate site, I wanted to include a small copyright, or creative commons symbol in the corner of the image, which would then expand to show the license detail when hovered over. I chose to use CSS for the hover animations rather than javascript and I’m quite pleased with the result. Modern browsers get a nicely animated transition and older browsers simply display the information on hover. The license function can be extended to provide the data in different formats depending on the content’s needs. For a homage widget like the one below, a subtle copyright icon works well, for images, illustrations or figures within a document we may prefer to list all of the attribution data at the foot of the document in a list of references.

Here’s the attribution implemented on our document image component:

### Low impact development

Working in this way, we’re able to extend the functionality of the CMS without modifying the core product (which would complicate our upgrade cycle) because we’re making the assumption that these features will eventually be provided natively within the CMS. These functions enhance how we manage and use images, yet are lightweight enough to be stripped out and replaced by native functions if and when they become available.


## Coursefinder 2010 report

- Date: 2011-06-30

- Wayback URL: https://web.archive.org/web/20140713224958/http://coffeepowered.co.uk/2011/06/coursefinder-2010-report/

- Status: ok


I’ve quietly been collecting search data on the University of Leeds’ Coursefinder for a while now, and always wanted to pick out some interesting facts and figures, the following is a combination of search and analytics data from the entirety of 2010.

Sorry this is an image and not 'proper' data, I didn't have time to do it properly :(

(large version) (https://web.archive.org/web/20140108232755/http://coffeepowered.co.uk/wp-content/uploads/2011/06/Screen-shot-2011-06-29-at-15.38.00.png)


## Building a ‘killer coursefinder’

- Date: 2011-06-08

- Wayback URL: https://web.archive.org/web/20140713224958/http://coffeepowered.co.uk/2011/06/building-a-killer-coursefinder/

- Status: ok


Killer Course Finder (https://web.archive.org/web/20140108232220/http://vimeo.com/24728688) from Jadu (https://web.archive.org/web/20140108232220/http://vimeo.com/jadu) on Vimeo (https://web.archive.org/web/20140108232220/http://vimeo.com/).

This is a presentation I delivered at CISG 2010 (https://web.archive.org/web/20140108232220/https://www.ucisa.ac.uk/en/groups/cisg/Events/2010/cisg2010.aspx) in Brighton, and Online Information 2010 (https://web.archive.org/web/20140108232220/http://www.online-information.co.uk/online2010/conference.html) in London late last year. This was my first foray into public speaking and I had an absolute blast and received some great feedback from the attendees. This session covers Coursefinder, probably the project I’m personally most proud of, and is about 50% what’s been done so far, and 50% what I’d love to do next. (I do go on a bit of a rant at 16 minutes in).

>

A university course finder is a phenomenally important tool, the internet makes it possible for a prospective student to evaluate courses from an array of Universities from the comfort of their bedroom, perhaps without ordering a printed prospectus
…perhaps without putting on trousers

Big thanks to the guys and girls at Jadu (https://web.archive.org/web/20140108232220/http://www.jadu.net/)for the speaking opportunity and for producing the video.


## Working to a structured development process

- Date: 2011-01-05

- Wayback URL: https://web.archive.org/web/20140713224958/http://coffeepowered.co.uk/2011/01/working-to-a-structured-development-process/

- Status: ok


You might work on small projects or large scale developments, you might be the only person involved or you might work with many others, regardless of your situation, having a structured development process is essential.

I work for the University of Leeds as a generalist designer/developer, a recent project of mine has been upgrading our institutional Content Management System to the latest version of the software, a task which had an extremely tight timescale which was met by using a structured development process.

### My toolbox

So let’s set the scene, I work within the Central IT Services’ Web Team and am the technical lead for the University of Leeds’ corporate website (www.leeds.ac.uk), this site runs on top of the Jadu Content Management System and was launched in September 2009. We have just performed a major upgrade of the core Jadu CMS which was turned around in a very short space of time, and it’s this upgrade project which is the basis for this post.

University of Leeds (www.leeds.ac.uk)

For those of you wanting to know which apps and tools I use, here’s a quick rundown:

- iMac 21.5″ 3.2GHz Intel Core i3

- Textmate (https://web.archive.org/web/20131215161936/http://macromates.com/)

- Terminal

- MAMP (https://web.archive.org/web/20131215161936/http://www.mamp.info/en/index.html) (local Apache/MySQL server)

- GIT (https://web.archive.org/web/20131215161936/http://www.sequelpro.com/>Sequel Pro (MySQL OSX user interface)
-

“There are a whole host of tools available which will allow you to manage your project, both free and paid-for.”

As well as using Trac internally within our team we have opened up access to a couple of teams within the institution who work with us on the corporate project. The Central Communications team (Comms), for example, have the ability to assign and manage tickets, see the commit history and timeline and read the wiki, but don’t have access to the source code repositories or source browsing facility through Trac.

### local > staging > production (aka develop > debug > deploy)

There are three separate environments which I use to develop for leeds.ac.uk. Firstly, all of the code I write is done on a local server which runs a complete standalone version of the code and database. This allows me to mess around as much as I want without any risk to the live site and database which runs on the production server where the live version of leeds.ac.uk lives.

In between my local development server and the production server is the ’staging’ server, this is an identical environment to the production server (even running on the same physical hardware) and is accessed through a private URL. By running this staging server I can deploy code for the team to test, confident that this is identical to how the site will operate once deployed to the production server.

The deployment is handled through the GIT version control system which is tied to our Trac system where we maintain a central source code repository (even though it’s not strictly needed with GIT, we still maintain a central repo for ‘disaster planning’), code is pushed from Local to Trac, then from Trac to Staging and ultimately from Trac to Live.

### How it all tied together

During the upgrade project I worked with our internal project co-ordinator and the Comms team to define a set of milestone dates for the project, such as ‘testing’, ‘pre-launch’, ‘launch’ and ‘post launch’.

We knew the date the site had to launch by was concrete, so worked backwards from there, with the pre-launch milestone set to the start of the week of launch, this contained any issues and tasks that needed to be completed before we could possibly go-live (such as a last minute content-freeze and migration from the currently live site to the upgraded site). Finally, the post-launch milestone allowed me to keep any tasks that weren’t directly related to the launch to be processed afterwards.

>

“We knew the date the site had to launch by was concrete,

so worked backwards from there”

We had a thorough round of testing in the weeks running up to launch, the task of testing was performed by Comms who were testing against a ‘release candidate’ build on the Staging server. They worked for a week going through every single page on the Release Candidate build and logged tickets for any bugs, whether they be for differences in layout or differences in content. This is a critical step and their eagle eyes spotted a wide range of issues, from missing/out of date content, to the fact that the breadcrumb trail was 2 pixels further to the right than it should be.

These issues were all classified against a simple priority scale:

- Blocker (the site can’t possibly go live until this is fixed)

- Critical (if this isn’t fixed, people may die)

- Major (it’s a big problem, but no-one’s going to die)

- Minor (this needs fixing at some point)

- Trivial (no-one would probably notice except us)

>

“a ‘critical’ issue may be seen as one which would cause the institution to cause severe confusion or lose money”

If you were to take into account the business considerations, a ‘critical’ issue may be seen as one which would cause the institution to cause severe confusion or lose money (such as printing an incorrect emergency phone number). Not all content is created equal, so a content difference on the Press Releases page might be classed as ‘Major’ while a page buried in the bowels of the site with a spelling error might be classed as ‘Minor’ or ‘Trivial’. It’s worth sitting down with the people who are going to be creating most of your tickets and defining what your priorities are to make sure that everything is not logged as high-priority to try and get them finished quicker.

(Based on this project I may move to remove the Blocker priority, as nearly all critical issues could be considered blockers)

I left the team alone for a week to perform their testing, only stepping in to fix any Blocker/Critical issues which would hamper their testing efforts and being on hand to answer any questions they had, after they were satisfied the entire site had been tested, their access to staging was revoked while I worked through all of the tickets assigned to the ‘Testing’ milestone. This process took 3 days for a couple of hundred issues, once the reported issue had been resolved the ticket was re-assigned to the owner for them to recheck the issue, and for them to close the ticket if it was fixed, or fail if it was still present.

### Make your tools work for you

I am lucky to work with some extremely talented people, including a colleague who installed and maintains our Trac instance and implements some of the weird and wonderful ideas we have to make it more useful for us. One of the most used tweaks was to use the post-receive hooks of GIT to allow us to modify tickets based on the commit message.

For example, I accept Ticket #356 which requires a code change to resolve. I make the required change to the code and commit this to my local repository with the following command:
1
git commit -m "Fixes #356 - bug was caused by ... and fixed by ..."

When I next push my changes to Trac, the post-receive hook recognises the ‘Fixes #356′ part of the commit message, adds a comment to the ticket linking to the specific changeset and diff showing exactly what changed, and sets the ticket to ‘testing’ status, which then fires off an email to the ticket owner prompting them to test the fix and close the ticket if it’s resolved.

I also communicated the progress of the project with the testing team by highlighting which version of the code the staging server was currently running:

Code version

This linked through to a summary changelog, which gave an outline of what had changed from version to version, clicking through would list precisely what had changed in the code and which tickets were fixed:

Trac changelog

We projected the Trac roadmap screen in our office with an auto-refresh which let us watch the testing milestone gradually reach 100% completion as the Comms team signed off the fixed tickets (I’m a sucker for visualising the size and progress of the task). All of this communication regarding the process of the project was passive, it was only available if and when anyone needed to see it.

Projection of project progress

### In conclusion

It doesn’t matter what tools or software you use as long as you’re able to make them fit around the way you work. If a piece of software gets in the way of how you work then you should seriously consider either changing it, or (if possible) changing the way it works to better suit your needs. If you’re working with other people on a project, communication is essential. By keeping everyone involved up-to date you can reduce the amount of time needed for meetings and reach that magical milestone, getting sign off.


## My year in moblogs

- Date: 2010-12-21

- Wayback URL: https://web.archive.org/web/20140713224958/http://coffeepowered.co.uk/2010/12/my-year-in-moblogs/

- Status: ok


As you may know, I run a small niche social site called homeofmuppets, the main feature of the site is the moblog which has been around since 2005 or so. This site has, over the years, become a photo record of my life, as it’s built around the friends that I know and love in real life, we use the site to share our experiences around the world, and it’s amazing to walk back through the years and remember these moments.

This year has been one of massive change and random moments so I thought I’d highlight some of the high points. Rather than sit here and write, I thought I’d let the moblogs do the bulk of the talking.
January - We started the year as we ended it, with lots and lots of snow (https://web.archive.org/web/20110919030134/http://www.homeofmuppets.com/moblogs/view/11417)

January - We started the year as we ended it, with lots and lots of snow

February - We celebrated 200 episodes of the Boagworld.com podcast with a mammoth live stream from The Barn

March - We met a dood from Boyzone

March - I finally made the switch!

June - We reunited with old friends from Toronto and Belgium

June - I married the love of my life

June - we became parents-to-be

November - I did my first conference speaking gig

November - I rocked a tux at my first black-tie dinner

December - At the ripe old age of 29, we got our first car!

December - The snow & ice descended to usher out 2010


## Playing with the Lumix LX3

- Date: 2010-06-30

- Wayback URL: https://web.archive.org/web/20140713224958/http://coffeepowered.co.uk/2010/06/playing-with-the-lumix-lx3/

- Status: ok


On June 10th I married the love of my life, and as a truly superb wedding present, she bought me a shiny new Lumix LX3 digital camera which I’ve been getting to grips with over the past few weeks.

The last digital camera I owned was a Canon Ixus 40 which was a nifty little thing but wasn’t much more than a regular point & shoot. The LX3 is still a compact, but is nestled at the top end and is about as high as you’d want before making the leap to a DSLR.

The look and feel is gorgeous, the metal body has a retro feel to it and it’s got a wide angle Leica lens which can shoot in a few different formats, my favourite is definitely the 16:9. The one downside is that there’s a very small zoom on the lens which is only useful for framing, other than that, I’m a big fan so I thought I’d share some sample shots I took before the wedding and on the honeymoon. All of these are unedited and straight from the camera.

I definitely prefer portrait photography to be in black & white and the LX3 has a very nice dynamic B&W mode which ups the contrast for a more moody shot.

P1000943 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4741474287/)

Nat on the London Underground (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4742094506/)

P1000175 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4742299406/)

P1000219 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4741672905/)

P1000232 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4742311284/)

There’s tons of settings to mess about with the exposure, as well as the ability to shoot in RAW mode to capture all that detail. this 10mp long exposure is best viewed LARGE! (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4741469353/sizes/l/in/photostream/)

Singapore at night (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4741469353/)

Colour reproduction is great, and very accurate to the scene

P1010772 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4742131900/)

And the macro mode is fantastic for those close ups

P1010900 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4741498545/)

P1010243 (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/paulstanton/4741482559/)

All in all, I love the camera and I’m hoping to take it with me quite often to capture some great shots. I might even invest some money as you can trick it out quite a bit with accessories!

Lumix LX3 fully loaded (https://web.archive.org/web/20140726210413/http://www.flickr.com/photos/nokton/3106803477/)


## Project52 fail

- Date: 2010-03-03

- Wayback URL: https://web.archive.org/web/20140713224958/http://coffeepowered.co.uk/2010/03/project52-fail/

- Status: ok


So at the start of the year I pledged my allegiance to the #p52 movement and aimed to write 1 new blog post per week for a year.

I failed.

So this is where I recant multiple excuses to explain my failure. While I got off to a good start with some posts that generated a fair number of comments everything seems to be happening at once and the amount of ‘free’ time I can devote to writing has all but vanished into thin air for a short while. As well as some new projects coming my way in my ‘day job’ which I’ve been working flat-out on for a couple of weeks I’ve also started to dip my toe back into the freelance waters and have been working on a couple of small projects on an evening as well as off bits of wedding planning here and there and the odd job interview to mix things up a bit leaving very little time to blog. Plus (and I know @garyvee might disagree) there’s 24, Lost and a whole host of other fine television programming which demand my attention.

I do plan on, and want to write regularly but once a week just doesn’t seem sustainable for a whole year, life and work will invariably get in the way. I’d rather take the time to write posts than crack out half-assed ones every week. So I’m handing in my #p52 membership card and commemorative plate and will be writing when I can from now on.


## Quick and dirty dropdown pagination in CakePHP

- Date: 2009-10-15

- Wayback URL: https://web.archive.org/web/20110110042654/http://coffeepowered.co.uk/2009/10/quick-and-dirty-dropdown-pagination-in-cakephp/

- Status: ok


I’ve been slowly rebuilding my Moblog (https://web.archive.org/web/20110821215205/http://homeofmuppets.com/moblogs) application using the CakePHP framework over the past year when I have the time and motivation. Over the past few evenings I’ve been refining a small element of my Moblog site which has started to dramatically increase user interaction with the site and allow old content to bubble back up to the top.

The Cake paginator helper (https://web.archive.org/web/20110821215205/http://book.cakephp.org/view/656/Methods) works fine if you’re using basic anchor links to trigger sort options, but I wanted to use a dropdown select element so that the user can choose how to order the moblogs.

So I know this is most likely a horrible solution to the problem and certainly not very ‘cakey’, but it’s quick, dirty, and it works for what I need it to do.

In the view we need a valid form element, even though the javascript hijacks the onChange event and doesn’t actually post the result. At the moment this does mean that this doesn’t work without javascript but I plan on improving this soon by only using $paginator->sort links in the view, and replacing them with the form completely in javascript.

in the view:

<?=

	$form->create('Moblog', array(

		'action' => 'index',

		'controller' => 'moblogs',

		'type' => 'get',

		'div' => false

		)

	);

?>

<?=

	$form->input('order',array(

		'label' => 'sort:',

		'options' => array(

			'modified' => 'recent activity',

			'id' => 'date added',

			'commented' => 'last commented',

			'moblog_comment_count' => 'most commented',

			'rand()' => 'random'

			),

		'selected' => $this->params['order'],

		'div' => false

		)

	);

?>

<?= $form->end('go'); ?>

In the jQuery we take whichever value was selected on change, build the relevant ‘paginator compatible’ url which the helper will use to return the required data on page load and then redirect the browser.

jQuery:

$('#MoblogOrder').change(function() {

	var url = '/moblogs/index';

	switch ($('#MoblogOrder option:selected').val()) {

		case 'modified':

			url += '/page:1/sort:modified/direction:desc/';

			break;

		case 'id':

			url += '/page:1/sort:id/direction:desc/';

			break;

		case 'commented':

			url += '/page:1/sort:commented/direction:desc/';

			break;

		case 'moblog_comment_count':

			url += '/page:1/sort:moblog_comment_count/direction:desc/';

			break;

		case 'rand()':

			url += '/page:1/order:rand()/';

			break;

		default : url += '/page:1/sort:modified/direction:desc/';

	}

	window.location = url;

}

In this particular example, I’m using a random order also, which needs to be an ‘order’ param instead of a ‘sort’, so in the controller I’m checking which params are being used, and setting a consistant order variable which is used in the view to maintain the selected state of the select element.

in the index method in the controller

function index() {

	if (isset($this->params['named']['sort'])) {

		$this->params['order'] = $this->params['named']['sort'];

	} elseif (isset($this->params['named']['order'])) {

		$this->params['order'] = $this->params['named']['order'];

	} else {

		$this->params['order'] = 'modified';

	}

}

If any Cake ninjas are reading this and have any suggestions, or better methods, please do leave a comment!


## The best quotes from FOWA

- Date: 2009-10-06

- Wayback URL: https://web.archive.org/web/20110110042654/http://coffeepowered.co.uk/2009/10/the-best-quotes-from-fowa/

- Status: ok


This years Future of Web Apps conference was an absolute blast, I’m hoping to give a full write up of my experience, but for now, here’s a list of my favourite quotes from the two days.

>

Stop thinking you understand your users.

Kevin Rose

>

Don’t build anything you don’t need for launch.

Mike McDerment

>

jQuery is like cocaine. One line will get you hooked.

Dustin Diaz

>

Metaprogramming is like trying to do crack cocaine responsibly.

Dustin Diaz

>

The web is too important to be owned by one vendor.

Bruce Lawson on Canvas vs. Flash

>

The great thing about standards is that there’s so many of them.

Aza Raskin on the number of OpenID providers

>

Marketing is the cancer on the nutsack of creativity.

Alex Hunter

>

Look after your users’ best interest, not yours.

Alex Hunter

>

If you keep pounding someone, they will come.

Gary Vaynerchuck

>

Customer service is not a fucking little “feedback” link in the corner of your website!

Gary Vaynerchuck


## Deliciously Timed Tweets

- Date: 2009-09-29

- Wayback URL: https://web.archive.org/web/20110110042654/http://coffeepowered.co.uk/2009/09/deliciously-timed-tweets/

- Status: ok


### What is it?

Deliciously Timed Tweets (or DTT for short) is a collection of API’s which allow you to bookmark links in Delicious (https://web.archive.org/web/20110920052019/http://delicious.com/), and then automatically tweet them at a specified time interval.

### What’s the point?

Delicious does already allow you to tweet your bookmarked links, the only problem is that this can result in Twitter spam if you bookmark lots of links in quick succession. DTT queues up your recent bookmarks, and allows you to specify a rate (say, every 60 minutes) for them to be tweeted at.

DTT powers the @boaglinks (https://web.archive.org/web/20110920052019/http://twitter.com/boaglinks) twitter feed.

### What do I need?

- PHP 4+ with cURL support

- MySQL

- Access to cron (https://web.archive.org/web/20110920052019/http://en.wikipedia.org/wiki/Cron)

- A Delicious (https://web.archive.org/web/20110920052019/http://del.icio.us/) account and some bookmarks.

### How do I get it?

Git : git clone http://coffeepowered.co.uk/labs/dtt/.git

Zip : http://coffeepowered.co.uk/labs/dtt/dtt.zip

Tar : http://coffeepowered.co.uk/labs/dtt/dtt.tar

### How do I install it?

- Grab the source from any of the locations above and extract/upload it to a location on your own server

- Modify config.php with your own details

- CHMOD install.php to 755

- Visit the install.php file in your browser (http://yoursite.com/path/to/file/install.php)

The default setting is for DTT to sync with delicious every hour, and new bookmarks will be tweeted out at a an rate of 1 per hour.

### Support?

Officially, this is provided “as is” and is an unsupported script, however I’ll endeavour to provide support for anyone who does have problems but I can’t promise anything!


## Lose the snooze

- Date: 2009-08-21

- Wayback URL: https://web.archive.org/web/20110110042654/http://coffeepowered.co.uk/2009/08/lose-the-snooze/

- Status: parse_failed


[No clean body recovered]


## New stylings

- Date: 2009-08-13

- Wayback URL: https://web.archive.org/web/20110110042654/http://coffeepowered.co.uk/2009/08/new-stylings/

- Status: ok


As you can see, I’ve been tinkering with a new theme for the blog! Please feel free to let me know what you think! I’ll be using the same leathery style on the Coffeepowered frontpage also, once the blog is done :)

### Disclaimer!

This theme isn’t finished, isn’t cross-browser tested and probably doesn’t validate. It’s to be considered a work in progress which I was just too impatient to keep hidden.


## Printable logos

- Date: 2009-08-07

- Wayback URL: https://web.archive.org/web/20110110042654/http://coffeepowered.co.uk/2009/08/printable-logos/

- Status: ok


This is one of those tips where I think “surely everyone knows this already?” but it’s a solution to a problem that I found which was quite neat and I’ll use all the time from now on.

When it comes to embedding a company logo into a page, quite often the logo won’t be suitable for print. For example, the website may be dark and the logo might be light and while this works fine when the site is viewed on-screen, it can look out of place when used in a print stylesheet or if the site is viewed with CSS disabled.

While building the new University of Leeds corporate website we got to the stage where we needed to build our print stylesheet, the page header has a white logo on a dark background.

Originally, the logo was inserted into the design using a standard CSS image-replacement technique:
1
2
3
<div id="logo">

    <h2><a href="http://www.leeds.ac.uk">University of Leeds</a></h2>

</div>
1
2
3
4
5
6
#logo a {

    background: url(logo_black.png) no-repeat;

    height: 53px;

    text-indent: -9999px;

    width: 184px;

}
Light logo on dark header

Light logo on dark header

When you’re using a CSS image replacement, the image doesn’t exist in the markup, it’s applied as a background image and only the h2 text is displayed. We toyed with the idea of using the same image replacement technique in our print.css, replacing the logo with the black-on-white variant. This quickly fell on it’s arse, as most browsers are set by default to not print background images as seen below.
Image replacement with CSS disabled

Image replacement with CSS disabled

### Putting the image back into the markup

In order to get around this, we decided to stop using image replacement and go back to having the image in the markup. Initially I was curious as to the effect of this from an SEO standpoint and had a quick chat with an SEO friend (https://web.archive.org/web/20100904222857/http://thehodge.co.uk/) about the disadvantage of not having our corporate logo as a heading. He pointed out that there would be no disadvantage to us as we’re not trying to rank on the ‘University of Leeds’ as a keyword and that as it’s mentioned everywhere else in the thousands of pages we manage, it’s not going to make a difference. (Your mileage may vary and this might not be suitable for everyone)
1
2
3
<div id="logo">

    <img src="logo_black.png" alt="University of Leeds logo" />

</div>

### Doing it bass-ackwards

Once we’d put the image back into the markup, it showed up as expected in our print stylesheet, however our white-on-black logo wasn’t really suited.
Same logo with CSS disabled

Same logo with CSS disabled

We already knew that we couldn’t use CSS to replace this with the black-on-white logo in our print.css, so we decided to do it the other way round. Rather than the have the white-on-black logo as default, we changed to having the black-on white as the default meaning that our no-css and print.css got the correct logo. We used a “hidden” class so we could hide the default image and a CSS overlay on the anchor tag to bring back our white-on-black logo to fit in with the rest of the design.
1
2
3
4
5
<div id="logo">

    <a href="http://www.leeds.ac.uk">

        <img class="hidden" src="logo_white.png" alt="University of Leeds logo" />

    </a>

</div>
1
2
3
4
5
6
#logo a {

    background: url(logo_black.png) no-repeat;

}

.hidden {

    display: none;

}
Light logo on dark header

CSS enabled
Black on white logo

CSS disabled / print stylesheet

### Conclusion

Because most browsers disable background images when printing by default, you need to be aware that any important images that are using image-replacement techniques may not work. Working around these limitations is possible with a bit of planning.


## Featured : Designers scribbles

- Date: 2009-08-06

- Wayback URL: https://web.archive.org/web/20110110042915/http://coffeepowered.co.uk/2009/08/featured-designers-scribbles/

- Status: parse_failed


[No clean body recovered]


## Meaningful milestones

- Date: 2009-08-06

- Wayback URL: https://web.archive.org/web/20110110042915/http://coffeepowered.co.uk/2009/08/meaningful-milestones/

- Status: ok


For the past 12 months I’ve been working exclusively on the same project, if you follow me on Twitter (https://web.archive.org/web/20100312135849/http://twitter.com/stanton) (and if you don’t, you really should) you might have heard me refer to it as Überproject as it’s without doubt the biggest project I’ve ever been involved with in my career so far.

It’s handover time for Überproject and as we’re wrapping up our development I’ve been taking stock of the last 12 months and thinking along the lines of “If we had to do this all over again, what would we do differently?” aka “What gave us grief, and how can we avoid doing it again”.

### Meaningful milestones

One particular aspect of Überproject was a large section of bespoke functionality which was, in effect, a project within a project which I’ll refer to as #up1 for the purposes of this blog (It’s not gone public yet, so I can’t name it specifically).

Early on, we attached two milestones to key stages in the project, a testing milestone, and a go-live milestone.

The testing milestone was defined as a date when functionality was to be delivered to our development environment ready to be put through it’s paces where any bugs would be logged as tickets in Trac (https://web.archive.org/web/20100312135849/http://trac.edgewall.org/) (our project management / source control platform) and we would then work through any outstanding tickets before the go-live milestone date.

#up1 was given milestones consistent with the rest of the project with a couple of months between testing and go-live, the development of the back end was going well and the front end development would be taken care of later with the rest of the front-end build (which had it’s own milestone).

About a week before the testing milestone was due for #up1 I was hit with a bombshell. The definition of ‘testing’ in this instance meant that the back-end had to be fully functional and production-ready for the end-users to start populating the module with data. This meant that the back-end should have entered testing weeks ago and had bugs ironed out before the end-users ever got close. The back-end needed be go-live ready.

Fortunately, a week’s worth of frantic coding meant that I got #up1 fully functional before the users were allowed in and this was only done on a limited basis, users were aware that we were still in development and we turned the situation to our favour by deputizing them as bug testers by asking for and encouraging feedback.

### The moral of the story?

Going forward, we will need to be absolutely clear of what’s expected to be delivered at each milestone and avoiding vague terms like ‘testing’, as we’ve seen, the definition of testing can vary wildly between different aspects of the same project.


## Font sizes and accessibility

- Date: 2008-11-18

- Wayback URL: https://web.archive.org/web/20100312135832/http://coffeepowered.co.uk/2008/11/font-sizes-and-accessibility/

- Status: fetch_failed


[No clean body recovered]


## Contextual CSS

- Date: 2008-11-18

- Wayback URL: https://web.archive.org/web/20100312150549/http://coffeepowered.co.uk/2008/11/contextual-css/

- Status: fetch_failed


[No clean body recovered]


## Colouring in

- Date: 2008-11-18

- Wayback URL: https://web.archive.org/web/20100312150659/http://coffeepowered.co.uk/2008/11/colouring-in/

- Status: fetch_failed


[No clean body recovered]

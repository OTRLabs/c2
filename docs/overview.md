I am kinda interested in creating a commercial competitor to Cobalt Strike by Forta, or Mythic C2 framework 

I am really interested in offensive security, specifically advanced adversary emulation 

I would like to pursue this full time, and monetize this in a way that can support myself in a way that allows me to focus on development full time.


Moving forward:



Alright so my goal is to design an adversary emulation system which makes it’s focus on

- 1. operational security meaning that the operators should stay anonymous and evade attribution 
- 2. Accurate information and intelligence gathering in relation to various operations 

Some general qualities of this adversary emulation platform are:


1. it is designed to be highly modular, and extensible. This is done to ensure that customers can use their existing skills in software development and programming to enhance their experience with the platform 
	1. One example is cobalt strike aggressor scripts or metasploit modules. Both are well documented and designed in a way that allows users to create their own versions within the specified framework and build on the existing features 

# Tech Stack
The user experience seeks to be flexible but minimalist. Not overly minimalist, just no unnecessary design choices. We do not want things to be “in the way” so to speak. 

I intend to build this project as a web application using 
- Litestar as the backend 
- Vite 
- React
- ShadCN UI components 
- SQLalchemy + advanced alchemy for ORM with Postgres for the database management system 
- seaweed FS S3 for blob storage (items stored here are indexed in the Postgres database )

We are looking to create a collaborative environment where intelligence can be pooled into a centralized location allowing for organizations to communicate effectively to accomplish their many goals 


My general idea is that, organizations would have their own instance of the platform, which they would operate for a prolonged period of time 


Something we must consider is that there are many advantages to having longer term infrastructure and correlating larger quantities of data to ultimately provide better analytics and reporting to clients that organizations who use this platform are reporting to

This however can of course come with risks. You would not want to have this massive database fall into the wrong hands, and if not properly secured, this is more of a liability than an advantage 


For this reason the platform is designed to be run on multiple machines, make heavy use of virtualization, containerization and other isolation mechanisms. The idea is that we maximize the segregation tactics we employ to divide each micro service within the platform allowing them to communicate only in the required ways, meaning they cannot be easily hijacked to maliciously impact operations 


Beyond that we also want to integrate the use of proxies, VPNs and Tor. This will be especially useful for any network reconnaissance features we may integrate as well as exposing various services without opening these services up unnecessarily. Using hidden services is a great way to allow our various microservice systems to communicate 

Something we want to consider is that, it is likely considered “bad practice” to use the same hosts for scanning across multiple engagements. This may not always be the case but it is likely in our best interest to not be 
1. Scanning with our actual hosts, instead using VPNs & proxychains 
2. Done from disposable environments only leaving behind the required amount of information on local host such as scan results 


I am considering using go-git to add a git integration for version control for software development, allowing organizations to develop their capabilities outside of the public view in places like GitHub 

In terms of architecture I think I am aiming for more of a modular monolith, where we have a single codebase that is broken up into many different services. This is done to ensure that we can easily deploy and scale the platform as needed.

The way I imagine this is a sort of "plugin" based system, where the core litestar app is the main service, and then we have many other services that can be added on to the core system.

This will of course be done using containers, and we will use docker-compose to manage the various services that make up the platform.

This includes things like the web server, the database, the file storage, the git server, the tor proxy, the VPN, the C2 listeners for communicating with implants, the various microservices that make up the platform, etc.



—- 
Overall, the above rough draft outlining the basic ideas of what I am looking to create is extremely incomplete and incoherent. I don’t think I even mentioned I wanted to make this system a micro service architecture until talking about how they should communicate over tor

Moving forward, what I can tell you is I am looking to build an adversary emulation platform that acts almost like an intranet or like, Microsoft office Suite specifically for an advanced persistent threat. Basically everything you would expect with an office suite plus the APT emulation 

Like I want to include core collaboration, project management, communication features 

As well as the ability to manage things such as port scanning or other automated intelligence gathering that an APT might do. 

Please help me create a more comprehensive outline of this plan
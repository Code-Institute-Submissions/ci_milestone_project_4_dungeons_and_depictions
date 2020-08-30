----INSERT AM I RESPONSIVE IMAGE HERE**----

Dungeons & Depictions

by Donal O'Farrell

Milestone Project 4: Full Stack Frameworks with Django - Code Institute

Dungeons & Depictions is a Dungeons & Dragons (D&D) character art site with an e-commerce poster store, the ability to commission your own artwork and an active blog.  Payments are made through Stripe. It is fully responsive across a large range of devices.

This project is for education purposes only.

[Explore the site here.](https://dungeons-and-depictions.herokuapp.com/)
 
## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Developer Goals**](#developer-goals)
    - [**Site Owner Goals**](#site-owner-goals)
    - [**User goals**](#user-goals)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Database Schema**](#database-schema)

3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
 
4. [**Technologies used**](#technologies-used)
 
5. [**Testing**](#testing)
    - [**Code Validators**](#code-validators)
    - [**Testing Devices**](#testing-devices)
    - [**Testing Browsers**](#testing-browsers)
    - [**Testers**](#testers)
    - [**Feature Testing**](#feature-testing)
    - [**Difficulties Encountered**](#difficulties-encountered)
 
6. [**Deployment**](#deployment)
    - [**How to run this project locally**](#how-to-run-this-project-locally)
 
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

--- 
## UX
 ---
 
#### Project Goals
There are currently an estimated 13.7 million active tabletop Dungeons & Dragons players worldwide. Since the inception of D&D in 1974, that number has continued to grow. And with D&D becoming more mainstream, projections are that the number of D&D players will continue to rise.

This project aims to create a site where D&D players can purchase posters, get their own unique one made and a community can form via the blogs for people who love the game.
 
#### Developer Goals
The developer's goal was to make a Full Stack Frameworks Django project for portfolio purposes.

The developer is also a frequent player of Dungeons & Dragons and a lover of artwork so the two things come together.
 
#### Site Owner Goals
The site owner's goal would be to have a place to where customers can place new character artwork commission with them, to sell the commissions they had previously created as posters and a blog to enchance SEO of site to attract more business.
 
#### User Goals
The user's goal is purchase new D&D artwork and to be able to have their own character artistically brought to life.

#### User Stories
Users stories can be found [here](https://docs.google.com/spreadsheets/d/1DikEybIFIieRvgfEDZgwBejrBPHho1Zs9w43oSDUnnY/edit?usp=sharing) on an external Google doc.
 
#### Design Choices
Dungeons & Depictions as designed to be responsive on desktop and across a range of smaller viewing devices. The smaller screens incur a change of navbar layout, footer content and various font and image size adjustments.

**Font** 
- MedievalSharp was chosen as to keep the fantasy theme across the site. Sans Serif was chosen as a fallback as its a safe, universally readable font.

**Icons** 
- The icons were all chosen for their obvious, commonly used meanings.

**Colours** 
- #9d0a0e shade of red was chosen as its this red that's heavily used across the D&D player handbooks and numerous manuals so users would have a strong assoication with it.
-  #e7e7db shade of grey was used for the navbar and footer elements as adds a nice contrast against center focus of white and its not too dominating to distract from anything.
- Standard css black was used across the site as font color and buttons. Its easy to see and contrasts nicely againt the red and white.

**Styling** 
  - Colours were kept as consistent as possible with also taking in visibility vs the background into consideration. 
  - Where visibility was semi-problematic, hover effects were added so these buttons would be more visible.

**Backgrounds:** 
- The background photo of the landing page was chosen as gave a strong intro to the artwork of the site and scaled nicely to mobile view.
- A white overlay was used for the other pages to enable clear viewing and strong contrast against buttons and artwork.

**Audio Files:** 
- No audio files were deemed necessary for this project and would just slow downloading speeds while being a distraction.
 
#### Wireframes
For the wireframes, [Balsamiq Wireframes](https://balsamiq.com/) was used as its quick and very simple.

All of my wireframes for this project can be found in the [design](design/wireframes/?raw=true) folder, which contains both the [desktop](design/wireframes/desktop/?raw=true) and [mobile](design/wireframes/mobile/?raw=true) sub-directories respectively.

---
## Database Schema
---

 INSERT DATABASE SCHEMA IMAGE HERE

---
## Features
---
### Existing Features

**Register Account**
- Anybody can register for free and create their own unique account. This is built using Django's authentication and authorization to validate profile data. Passwords are hashed for security purposes.

**Change Delivery Info**
- Users can update their delivery info on their profile page.

**View Showcase**
- On the showcase page, users can see all commissions done to date.

**Filter Showcase**
- Users can limit the showcase to show artwork of only characters by a certain class e.g. rogue.

**Search Showcase**
- Users can search the entire showcase for keywords such as elf or dwarf or by a specific character's name. Any keywords in the descriptions of the commissions can be found through this.

**View a Single Commission**
- From the showcase, users can click onto a specific commission to see its name, price, description.

**Add an Existing Commission to Cart**
- Users can add any of the existing commission to their cart to buy as a poster.

**Create a New Commission**
- Users can fill out a form and request a new commission specific to them. This creates a new commission which they then can add to cart as normal.

**Purchase Posters or New Commission via Stripe**
- Users can fill out a form and request a new commission specific to them. This creates a new commission which they then can add to cart as normal.


**View Blog**
- Users can view blogs by the artist.

**Comment on Blog Posts**
- Users can add comments to specific blog posts though these require approval by admin before being visibile.

**Admin Status**
- As Admin (ie: superuser), there are quite a few additional features across the site that no other user has access to such as creating or deleting users accounts and adding, editing or delete any commissions or blog posts.
- The navbar has an additional link to the Django Admin Panel and a link to quickly add a new commission to the showcase.
- Admins can edit aor delete commissions directly in the showcase.
- Admins approval is needed to approve any comments on blog.

### Features Left to Implement

**Users Being Able to Request Changes** 
- The user who commisssioned a new artwork would be able to see the progress of it and ask for minor changes to be made before completation.

**Postal Tracking Number**
- Users should be able to recieve a trackign number once products had been posted out to them.

**Delete Account**
- Users should be given the opportunity to delete their account entirely. Currently they can register and edit their data, but not remove it from the database.
---
## Technologies Used
 ---
- [Gitpod](https://gitpod.io/workspaces/) 
    - Developer used **Gitpod** for their IDE while building the website.
- [GitHub](https://github.com/)
    - This project uses **GitHub** to store and share all project code remotely. 
- [GIMP](https://www.gimp.org/)
    - This project uses **GIMP** for photo editing needs. 
- [Balsamic](https://balsamiq.com/)
    - This project uses **Balsamic** to do all wireframes. 
### Front-End Technologies
- [Bootstrap](https://getbootstrap.com/)
    - This project uses **Bootstrap** as its base framework.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - Used as the base for markup text.
- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
    - Used as the base for cascading styles.
- [Bootstrap](https://getbootstrap.com/)
    - This project uses **Bootstrap** as its base framework.
- [Stripe](https://stripe.com/)
    - Used to make secured payments for the e-cart.
- [Amazon AWS S3](https://aws.amazon.com/)
    - This project uses **AWS** to store its media and static files.
### Back-End Technologies
- [Python](https://www.python.org/)
    - Used as the back-end programming language.
- [JavaScript](https://www.javascript.com/)
    - Used as a secondry back-end programming language.
- [Django](https://www.djangoproject.com/)
    - Used as the Python web framework.
- [Heroku](https://heroku.com/)
    - This project uses **Heroku** to deploy its code.
- [PostgreSQL](https://www.postgresql.org/)
    - Used as relational SQL database plugin via Heroku.
---
## Testing
 ---
#### Code Validators
- [Dillinger](https://dillinger.io/)
This was used for Markdown in this README.md.
 
- [W3](http://validator.w3.org/)
This was used to check the HTML and CSS in this project.
 
- [JSHint](https://jshint.com/)
This was used to check the JavaScript in this project.

- [PEP8](http://pep8online.com/)
This was used to check the Python in this project.
 
#### Testing devices
- Desktop 
- iphone 6
- Huawei P30 lite
 
#### Testing Browsers
- Chrome 
- Safari
- Microsoft Edge
- Mozilla Firefox
 
#### Testers
Special thanks to:
- Amy Buckley
- Kevin O'Brien

#### Feature Testing
- **Browse All Mods:** All mods in the database appear and expand as intended.
- **Browse Mods by Category:** Mods break down accurately into their assigned categories and expand as intended.
- **Add Mods:** Mods added appear in the browse section after submission as well as behind the scenes server side on MongoDB in the correct assigned collection. All input fields must be filled in or the page won't submit.
- **Edit Mods:** All edits submit correctly and update the database as designed. All input fields must be filled in or the page won't submit.
- **Delete Mods:** Mods deleted are fully removed from browser search and from the database.
- **Category Control:** All categories create, edit and delete as intended. All input fields must be filled in or the page won't submit.
- **Register:** All new accounts made are uploading to the database 'users' with user name and encrypted password as intended. All input fields must be filled in or the page won't submit. If exact details are already in the database, it won't won't let you make an identical account.
- **Login:** Login will only happen if the correct username and password is submitted or else it returns that username/password is invalid.
 
#### Difficulties Encountered
- The dropdown menu for the categories wouldn't work on first click and always required a second one to open. This was solved on handy advice on Slack from Simon Castagna.
 
- Category_name exists in both 'categories' and 'mods' collections. This led to some confusion on appropriate pathing for functions. If redoing the project, these would have been merged.
 
- A flight flicker of the screen occurs in the category dropdown section when page first loads. This is thought to be caused by custom css overriding Materialize's default. This still needs to be fixed.
 
- The site has NOT been optimized for mobile devices. As a result there is text overspill from title and buttons not fitting well into containers. All functionality does work though.
---
## Deployment
 ---
### How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Gitpod](https://www.gitpod.io/).

The following **must be installed** on your machine:
- [PIP3](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 

### Instructions
1. Save a copy of the github repository located at https://github.com/dof-bull/ci_milestone_project_3_rimworld_mod_locker by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/dof-bull/ci_milestone_project_3_rimworld_mod_locker
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip3 install --upgrade pip.
```

5. Install all required modules with the command 
```
pip3 -r requirements.txt.
```

6. In your local IDE create a file called `env.py`.

7. Inside the env.py file, create a MONGO_DBNAME variable and a MONGO_URI to link to your own database. Please make sure to call your database `rimworld_mod_locker`, with 3 collections called `categories`, `mods` and `users`. 

8. You can now run the application with the command
```
python app.py
```

9. You will get a pop up saying that a new port has been open and you can view it in your browser.

### Heroku Deployment

To deploy Rimworld Mod Locker to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip3 freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 8080

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, make sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.
 ---
## Credits
 ---
### Content

- Font Awesome for their icon set.
https://fontawesome.com/icons?d=gallery

- Google Fonts
https://fonts.google.com/specimen/MedievalSharp?query=mediev&sidebar.open=true&selection.family=MedievalSharp

- Trade Gecko - SKU Generator
https://www.tradegecko.com/free-tools/sku-generator

- Fantasy Name Generator
https://www.fantasynamegenerators.com/

- Stack Overflow for lesson on linebreaks.
https://stackoverflow.com/questions/37133336/new-line-on-django-admin-text-field?rq=1

- CSS-tricks for the lesson on a CSS triangle.
https://css-tricks.com/snippets/css/css-triangle/

- Hello Web Books for the quick tutorial on contact forms.
https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/

- Django Central for the tutorial on blog making on adding a comment system.
https://djangocentral.com/building-a-blog-application-with-django/
https://djangocentral.com/creating-comments-system-with-django/

- DungeonVault for article on estimated playerbase.
https://dungeonvault.com/how-many-dnd-players-are-there-worldwide/

### Media
All character artwork belongs to their respective owners and is not being used in any commercial way in this educational project.

- https://www.pinterest.ie/pin/169659110948340088/
- https://imgur.com/gallery/6ZsUUWP
- https://www.clipartkey.com/view/immxTJ_silhouette-ork-fighter-warrior-fantasy-silhouette-fighter/
- https://www.pinterest.ie/pin/480266747749452641/
- https://www.pinterest.ie/javidante/fantasy-barbarian/
- https://www.reddit.com/r/DnD/comments/5y1dia/art_my_first_commissioned_character_bard/
- https://www.pinterest.ie/pin/550142910729952693/
- https://www.pinterest.fr/pin/382383824602593811/
- https://www.pinterest.ie/pin/632403972652614202/
- https://www.pinterest.ie/questinggm/druid/
- https://www.pinterest.ie/questinggm/druid/
- https://www.pinterest.ie/pin/656892295625221662/
- https://www.pinterest.ie/pin/480266747747022370/
- https://www.pinterest.ie/mrtomsaunders/monk/
- https://www.pinterest.ie/pin/401664860509053358/
- https://www.pinterest.ie/pin/787426316075272935/
- https://www.pinterest.ie/pin/504543964488212711/
- https://www.pinterest.ie/pin/634796509950001637/
- https://www.pinterest.ie/pin/480266747763044267/
- https://www.pinterest.ie/pin/542683823841741064/
- https://www.pinterest.ie/pin/110690103324463688/
- https://www.pinterest.ie/pin/798474208907336085/
- https://www.pinterest.ie/pin/AaszQPIw-h6TMiEmDm0nNCB-N8jUWTQmoKnvwIE3Ul1SbZkjbYQZAyU/
- https://www.pinterest.ie/pin/379146862377938955/
- https://www.pinterest.ie/pin/171066485831631134/
- https://www.pinterest.ie/pin/480266747760576440/
- https://www.pinterest.ie/pin/819162619703363328/
 
### Acknowledgements
 
- Anthony Ngene as my project mentor and for his help and advice throughout the project.
(https://github.com/tonymontaro)
- Anna Greaves for her awesome README.md templates.
(https://github.com/AJGreaves)
- TravelTimN for his excellent README.md templates.
(https://github.com/TravelTimN)
 






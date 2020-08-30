![Dungeons and Depictions header image](media/readme_header_photo.jpg?raw=true "Dungeons & Depictions")

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

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
 
3. [**Technologies used**](#technologies-used)

4. [**Database Schema**](#database-schema)

5. [**Testing**](#testing)
 
6. [**Deployment**](#deployment)
 
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

--- 
## UX
 ---
 
#### Project Goals
There are currently an estimated 13.7 million active tabletop Dungeons & Dragons players worldwide. Since the inception of D&D in 1974, that number has continued to grow. With D&D becoming more mainstream, projections are that the number of D&D players will continue to rise.

This project aims to create a site where D&D players can purchase artwork posters, get their own unique character made as one and a community can form via the blogs for people who love the game and love drawing.
 
#### Developer Goals
The developer's goal was to make a Full Stack Frameworks Django project for portfolio purposes.

The developer is also a frequent player of Dungeons & Dragons and a lover of artwork so the two things come together.
 
#### Site Owner Goals
The site owner's goal would be to have a place where customers can place new character artwork commission with them, to sell the commissions they had previously created as posters and a blog to enhance SEO of the site to attract more business.
 
#### User Goals
The user's goal is purchase new D&D artwork and to be able to have their own character artistically brought to life.

#### User Stories
Users stories can be found on an external Google doc  [here](https://docs.google.com/spreadsheets/d/1DikEybIFIieRvgfEDZgwBejrBPHho1Zs9w43oSDUnnY/edit?usp=sharing).
 
#### Design Choices
Dungeons & Depictions was designed to be responsive on desktop and across a range of smaller viewing devices. The smaller screens incur a change of navbar layout, footer content and various font and image size adjustments.

**Font** 
- MedievalSharp was chosen to keep the fantasy theme across the site. Sans Serif was chosen as a fallback as its a safe, universally readable font.

**Icons** 
- The icons were all chosen for their obvious, commonly used meanings.

**Colours** 
- `#9d0a0e`: ![#9d0a0e](https://via.placeholder.com/15/9d0a0e/000000?text=+) 
    This shade of red was chosen as it's this red that's heavily used across the D&D player handbooks and numerous manuals so users would have a strong association with it.
- `#e7e7db`: ![#9d0a0e](https://via.placeholder.com/15/e7e7db/000000?text=+) 
    This shade of grey was used for the navbar and footer elements as it adds a nice contrast against the center focus of white and it's not too dominating to distract from anything.
- `#000000`: ![#000000](https://via.placeholder.com/15/000000/000000?text=+) 
    Black was used across the site as font color and button highlighting. It's easy to see and contrasts nicely against the red and white.

**Styling** 
  - Colours were kept as consistent as possible with also taking in visibility vs the background into consideration. 
  - Where visibility was semi-problematic, hover effects were added so these buttons would be more visible.

**Backgrounds:** 
- The background photo of the landing page was chosen as it gave a strong intro to the artwork of the site and scaled nicely to mobile view.
- A white overlay was used for the other pages to enable clear viewing and strong contrast against buttons and artwork.

**Audio Files:** 
- No audio files were deemed necessary for this project and would just slow downloading speeds while being a distraction.
 
#### Wireframes
For the wireframes, [Balsamiq Wireframes](https://balsamiq.com/) was used as it's quick and very simple.

All of my wireframes for this project can be found in the [design](design/wireframes/?raw=true) folder, which contains both the [desktop](design/wireframes/desktop/?raw=true) and [mobile](design/wireframes/mobile/?raw=true) sub-directories respectively.

---
## Features
---
### Existing Features

**Register Account**
- Anybody can register for free and create their own unique account. This is built using Django's authentication and authorization to validate profile data. Passwords are hashed for security purposes.

**Update Delivery Info**
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
- Users can fill out a form and request a new commission specific to them. This creates a new commission which can then be added to cart as normal.

**Purchase Posters or New Commission via Stripe**
- Users can fill out a form and request a new commission specific to them. This creates a new commission which they can then add to cart as normal.

**View Blog**
- Users can view blogs by the artist.

**Comment on Blog Posts**
- Users can add comments to specific blog posts though these require approval by admin before being visible.

**Admin Status**
- As Admin (ie: superuser), there are quite a few additional features across the site that no other user has access to such as creating or deleting users accounts and adding, editing or delete any commissions or blog posts.
- The navbar has an additional link to the Django Admin Panel and a link to quickly add a new commission to the showcase.
- Admins can edit or delete commissions directly in the showcase.
- Admins approval is needed to approve any comments on blog posts.

### Features Left to Implement

**Users Being Able to Request Changes** 
- The user who commissioned a new artwork would be able to see the progress of it and ask for minor changes to be made before completion.

**Postal Tracking Number**
- Users should be able to receive a tracking number once products have been posted out to them.

**Delete Account**
- Users should be given the opportunity to delete their account entirely. Currently they can register and edit their data, but not remove it from the database.

**Social Media Sign In**
- Users should be able to create an account via their social media account. Would make the sign in more streamline.

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
- [QuickDBD](https://www.quickdatabasediagrams.com/)
    - This project uses **QuickDBD** to do all database schemas. 
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
    - Used as a secondary back-end programming language.
- [Django](https://www.djangoproject.com/)
    - Used as the Python web framework.
- [Heroku](https://heroku.com/)
    - This project uses **Heroku** to deploy its code.
- [PostgreSQL](https://www.postgresql.org/)
    - Used as a relational SQL database plugin via Heroku.

---
## Database Schema
---

![Dungeons and Depictions Regional Schema](media/regional_db_schema.jpg?raw=true "[Dungeons & Depictions Regional Schema")

---
## Testing
---

The testing information can be found in this separated [Testing](TESTING.md) file.

All features working as expected bar one.

Last minute error has occurred where going into an individual blog causes a Server 500 error.
It has to be soemthing to do with Heroku's PostgreSQL as everything working fine on Gitpod Dev server.
This is very regretful as comment section on blog posts had been recently upgraded with using user's username for comments.

---
## Deployment
---
This project can be viewed live on Heroku: [https://dungeons-and-depictions.herokuapp.com/](https://dungeons-and-depictions.herokuapp.com/)

### How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Gitpod](https://www.gitpod.io/).

The following **must be installed** on your machine:
- [PIP3](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Save a copy of the github repository located at https://github.com/dof-bull/ci_milestone_project_4_dungeons_and_depictions by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command:
`git clone https://github.com/ci_milestone_project_4_dungeons_and_depictions`

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. If needed, Upgrade pip locally with:
`pip3 install --upgrade pip.`

4. Install all required modules with the command:
`pip3 -r requirements.txt.`

5. In your local IDE create a file called `env.py`.

6. Inside `env.py`, create a SECRET_KEY variable.

7. Make all migrations with the commands:
`python3 manage.py makemigrations`

8. Run all migrations with the commands:
`python3 manage.py migrate`

9. Now load the category data from the fixtures with:
`python3 manage.py loaddata categories`

10. Next load the commissions data (order is important!) from the fixtures with:
`python3 manage.py loaddata commissions`

11. You can now run the application with the command:
`python3 manage.py runserver`

13. You will get a pop up saying that a new port has been open and you can view it in your browser.

In order to access the Django *Admin Panel*, you must generate a superuser and assign an admin username, email, and secure password.
`python manage.py createsuperuser`


### Heroku Deployment

This part assumes you have already deployed the project locally first (see above).

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. Once you have the project setup locally, you can proceed to deploy it remotely with the following steps:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app:
`pip3 freeze --local > requirements.txt`

2. Create a **Procfile** to tell Heroku what type of application is being deployed using *gunicorn*, and how to run it and type into the file:
`web: gunicorn dungeons_and_depictions.wsgi:application`

3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
-
4. In the Heroku **Resources** tab, navigate to the *Add-Ons* section and search for **Heroku Postgres**. Make sure to select the free *Hobby* level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. 

5. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables. You will need to copy/paste the *.env* key value SECRET_KEY into the config variables.

6. Your app should be successfully deploying  to Heroku at this point but it's still missing some key features.

7. Update the *settings.py* file to connect the remote database using this Python package: `dj_database_url`

8. Re-build the migrations and create a superuser to your new remote database using the instructions in the *local deployment* section above.

9. Sign up for a free [Amazon AWS](https://aws.amazon.com/) account in order to host your *staticfiles* and *media* files. From the **S3 buckets** section, you'll need to create a new unique bucket. Follow these next steps to complete the setup:

**Permissions** > **CORS configuration**:

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

**Permissions** > **Bucket Policy**:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<x>/*"
        }
    ]
}
```

*! IMPORTANT ! - on the **Resource** line above, be sure to replace `<x>` with your **AWS bucket arn** details, but retain the `/*` at the end.* It should look similar to this:
    - `"Resource": "arn:aws:s3:::my-bucket-name/*"`

10. From here, you'll need to navigate to the **IAM** section of AWS.
    - Create a *New Group* and be sure to select your existing S3 Bucket details to attach.
    - Create a *New Policy* and a *New User* in the IAM section as well, then attach these to the Group you just built. From the new user you should get the below variables to add to your Heroku config vars:
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    You should also add the following config var to Heroku and set its value to `True`:
    - `USE_AWS`

11. In your CLI-terminal, you should now be able to push the static files to AWS if everything is configured properly using this command:
`python manage.py collectstatic`

12. Sign up for a free [Stripe](https://stripe.com) account. Navigate to the **Developers** section, and click on **API Keys**. Add these to your Heroku config vars. These keys are:
`Publishable Key`: **STRIPE_PUBLIC_KEYy**
`Secret Key`: **STRIPE_SECRET_KEY**

13. While in the  **Developers** section of Stripe, go down to Webhooks and click **Add endpoint** on the top right. Add the below as your webhook endpoint url and allows all events:
`https://dungeons-and-depictions.herokuapp.com/checkout/wh/`

14. To set up working emails, go to gmail.com and create an account.
    - Go to settings
    - Accounts and Imports
    - Other Google Account settings
    - Security
    - Turn on 2-Step Verification
    - This will unlock App passwords underneath
    - Create a new app password and note the given code
    
    Go to Heroku config vars and enter:
    `EMAIL_HOST_PASS` and your new password gmail gave you.
    `EMAIL_HOST_USER` and the gmail email account.

The site is now successfully deployed.

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

- Stack Overflow for the lesson on linebreaks.
https://stackoverflow.com/questions/37133336/new-line-on-django-admin-text-field?rq=1

- CSS-tricks for the lesson on a CSS triangle.
https://css-tricks.com/snippets/css/css-triangle/

- Hello Web Books for the quick tutorial on contact forms.
https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/

- Django Central for the tutorial on blog making on adding a comment system.
https://djangocentral.com/building-a-blog-application-with-django/
https://djangocentral.com/creating-comments-system-with-django/

- DungeonVault for the article on estimated player base.
https://dungeonvault.com/how-many-dnd-players-are-there-worldwide/

- Responsive Designs for their device responsiveness generator.
http://ami.responsivedesign.is/

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

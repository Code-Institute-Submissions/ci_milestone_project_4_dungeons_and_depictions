# Dungeons & Depictions - Testing

  - [Main README file](Readme.md)
  - [Live website](https://dungeons-and-depictions.herokuapp.com/)


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
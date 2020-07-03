# Building in Green
## Data Centric Development Project

### This is a Community platform for Green Builders enthusiast. The application displays 5 different pages: 
* Welcome page where the basic principles of a sustainable building are defined.
* Green Builders Community Gallery page where members of the Community can watch all the different Green Buildings from other members. 
* Green Building Details page to display the details of the selected Green Building.
* Add your own page allow user members to add their own Green Building to the Gallery of the Community. 
* Edit Green Building page which allow the members to edit or delete a Green Building of the Commnunity.

Live demo: [Building in green](https://bulding-in-green.herokuapp.com/)

The Website is developed by a Green Builder enthusiast for other sustainable and green makers enthusiasts.
The pourpose of this project is to have a showroom (database) of different sustainable and eco-friendly construction in a natural environment. 
To share ideas and find inspiration from others for their next build. This is a user-friendly application for users trying to be clean and easy to use.
All images and data used in this project are fictitious. 

### The main goal of this app is:

* Host a user-friendly environment which is intuitive by nature.
* Provide both front end usability and back end functionality to create a full application experience.
* Spread knowledge of green suitable construction.

### The user's goals are:

* Share their own Green Buildings and show them to the world.
* Learn and gain inspiration from other builders.

## UI

**Colors, Fonts & Layout**
The layout is based on a Theme template from startbootstrap.com.
Colors and Fonts from landing-page.css and mystyle.css to customize
the website.
**Responsiveness**
Using Bootstrap and mystyle.css to make a responsive layout from large to small size screens.


## UX

**Users:**
Any green builder who wants to share what they built. Developed only in English.
Green constructors enthusiasts who desire to share/watch/learn what others are building.
It is an intuitive and easy to use application where users can:
1. Read and learn about basis sustainable constructions prinpiples. 
2. Search and filter different types of green buildings of other users of the Community per 
   categories base on main material used. Each building/house 
   with their own features, pictures, materials, and descriptions. 
   Visitor can find "More Info." and have information about the house. 
3. Users can add their own Green Building including links to their own pictures and details as: 
   username, location, year of construction, name of the house and materials used. 
4. Users can also Edit a house from the data base or even deleted with warning alert about changes and deletion. 

**User stories:**
* As a first-time user, I want to view Green Buildings to get inspiration.
* As a first-time user, I want to use the platform to share my eco-friendly house.
* As a user, I want to add my house to the Community.
* As a returning, I want to update or delete my record, each user should be able to make changes only in their own houses.
* As an administrator, I want to be able change previous projects, upload new projects and clean the data base.

## Mockups
Balsamic initial design idea.

![Building in Green Wireframes](/static/img/WireframesBuildinginGreen.png)

## Features
### Navigation bar and footer 
We will find in all pages a Navbar with brand name (Building in Green), Home page, Gallery page where all the houses in the data 
base are displayed or selecting by categories (Wood, Cob, Stone or Upcycling, collection stored at MongoDB with categories name) displayed in a Dropdown.
And the final option of the navigation list is Add your own house Form.

We have also a footer in all pages where we have only a copyright statement. There is not option to contact or loging in this 
initial idea of the project. 

### Home
Shows basic sustainable principles of the Green Construction, with different images/icons/text. 
This a landing page base on Themes from startbootstrap.com

### Green Builders Community Gallery
Displays all the records of the Community. It is also possible to filter by category (Wood, Cob, Stone or Upcycling).
and it will display only the green constructions under the selected category.
We have a More Info. button, when clicked it will go to a new page View Green Building Details, where username, construction date, 
location and other details are displayed. 

### View more details
This is a card where all the information regarding this construction will be shown as:
* Image
* Category
* House name
* Username
* Construction date
* Location
* Description
Collection "houses" stored as a string at MongoDB.

We have 2 buttons:
* Delete: On click we will get and alarm with text:
 *This process cannot be undone! Are you sure you want to delete this house?* 
  with options to continue (OK) or cancel the operation. After clicking OK, open Home page.
* Edit: On click it will open a new page, Edit Green Building page.

### Edit Green Building
Displays a Form with select option and input fields to fill in the requested details.
Materializecss.com Form and jQuery initialization added.

We will find 2 buttons:
* Update: This button must be clicked to save the changes of the records. And an alert message will show:
  *Thank you! The building has been updated successfully.* After clicking OK, open View More Details page.
* Cancel: If we click on cancel, we will get and alert with the next message: 
  *Your building has not been edited.* After clicking OK, open View More Details page.
  

### Add your own
This is also a Form from Materialize with Select option and equired fieldss. We will find 2 buttons to:
* Insert: On click add the records to the data base of the Community, and you will see an alert with text:
  *"Thank you! The building has been added successfully."* After clicking OK, open View More Details page.
  where you can Delete or Edit the inserted data. To view your record added to the Community user has to click on:
  *To view your Green Building added to the Community visit the Gallery*
* Cancel: On click it will cancel the operation and nothing will be added to the data base. 
  Alert with the next message shown: 
  *Your building has not added.* After clicking OK, open Home page.

Visiting Green Builders Community Gallery, we will see that the new house is displayed at the end of the list. 
Or if you select a category it will be displayed at the end of the list under that category.

## Features to add in future
Add a Sign In/Sign Up option to create a real feeling of membership.
Restrictions to Edit or Delete base on membership.
Chat for the members to communicate between them. 

## Existing features
Navigation bar - Collapsible for small screens.
CRUD - Users can upload, read, update, and delete content in the database.
Sorting - Users can select diferent categories Building categories.

## Technologies used

This Green Building web application was built using:
### Languages:
**HTML5**, **CSS3**, **JavaScript** was used to build an interactive webpage.

**Python** was used to build the structure and functionality of the back end.

### Libraries to style interactive options:
* Startbootstrap
* Bootstrap CSS
* Bootstrap JS
* FontAwesome
* jQuery
* Dnspython
* Bootstrap and Materialize to make the structure and the site responsive in a simple manner. 
* Flask used to display python functions on the website.
* Pymongo to make the code written in python talk to the database.

### Tools:
**MongoDB** was used as the database host.

### Deployment/Host:

**Heroku** was used to deploy the live version of the application.

The website is built and developed using **GitPod** as IDE.

### Testing:
* W3C's HTLM Validator

* W3C's CSS Validator

* Responsinator 

* JSHint

## Deployment
GitPod was used as IDE to develop this application. Throughout the development, the project was 
committed to the git and continuously pushed automatically to Heroku connected to GitHub. 

**Deploy to Heroku**
Steps to deploy the application on Heroku:

* Login to my Heroku
* Click on "new" in the top right corner and choose "create new app"
* Choose the name of the application and set "Region" to Europe. Click "Create app"
* Go to settings and add the config vars PORT (5000) and IP (0.0.0.0)
* Login on Heroku through the CLI in your IDE.
* Add the project as a master branch
* Push to Heroku (git push)
* For Heroku to be able to run the app a Procfile and a requirements.txt must be created 
  which is done in the IDE. 

## Testing

**W3C's HTLM Validator** used to validate the websites HTML code.

**W3C's CSS Validator** used to validate the websites CSS code.

**JSHint** used to validate the websites JavaScript code.

**Responsinator** used to check responsiveness.

Pages work as expected in a responsive manner. All select options, forms and buttons tested. 
Only a function to clear the selected categories in the dropdown is yet to be implemented. 
When user select an option from the dropdown, after displaying the selection, dropdown does not show
all the possible options to selected again. User has to click any other nav link to refresh select options. 
Clear/refresh dropdown function must be implemented in future.

## Credits

**Content** 

All the text content on the website was written by me.

**Media**

Images used in the webpage were collected from unsplash.com.
Data on MongoDB non-real, written by me.

## Acknowledgements

Thank you very much to all Code Institute Team Tutors and my Mentor 
for his support, patience, and guidance throughout this project.

## Disclaimer
The content of this website is for educational purposes only.










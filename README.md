# Building in Green
## Data Centric Development Project

### This is a community platafform for Green Builders enthusiast. The application displays 5 different pages: 
* Welcome page where the basic principies of a sustainable building are defined.
* Green Builders Comunity Gallery page where members of the comunity can watch all the different Green Buildings from other members. 
* Green Bhuilding Details page to display the details of the selected Green Building.
* Add your own page allow user members to add their own Green Building to the Gallery of the Comunity. 
* Edit Green Building page which allow the members to edit or delete a Green Building of the Comnunity.

Live demo: [Building in green](https://bulding-in-green.herokuapp.com/)

The Website is developed by a Green Builder enthhuist for other sustainable and green contructors enthusiasts.
The pourpose of this project is to have a showroom (database) of different sustainable and eco friendly construction in a natural environment. To share ideas
and find inspiration from others for their next build. This is a user friendy application for users trying to be clean and easy to use.
All images and data used in this project are fictitious. 

### The main goal of this app is:

* Host a user-friendly environment which is intuitive by nature.
* Provide both front end usability and back end functionality to create a full application experience
* Spread knowledge of green suitable construction.

### The users goals are:

* Share their own Green Buildings and show them to the world.
* Learn and gain inspiration from other builders.

## UX

**Users:**

Any green builder who wants to share what they built. Developed only in English.
Green constructors enthuiasts who desiere to share/watch/learn what others are building.
It is an intuitive and easy to use application where users can:
1. Read and learn about basis susiatbale constructions prinpipies. 
2. Search and filter different types of green buildings of other users of the Comunity per 
   categories base on main material used. Each bulding/house with their own features, pictures, materials, and descriptions. 
   Visitor can find "More Info." and have information about the house. 
3. Users can add their own Green Building including links to their own pictures and details as: 
   username, location, year of construction, name of the house and materials used. 
4. Users can also Edit a house from the data base or even deleted with warning alert about the delection. 

**User stories:**
* As a first-time user, I want to view Green Buildings to get inspiration.
* As a first-time user, I want to use the platform to share my aco-friendly house.
* As a returning, I want to add my house to the Community.
* As a returning user, I want to be able change previous projects and upload new projects.

## Mockups
Balsamic initial design idea.

![Building in Green Wireframes](/Wireframes/WireframesBuildinginGreen.png)

## Features
### Navigation bar and footer 
We will find in all pages a Navbar with brand name (Building in Green), Home page, Gallery page where all the houses in the data 
base is displayed or selecting by categories (Wood, Cob, Stone or Upcycling) displayed in a Dropdown.
And the final option of the navigation list is Add your own house Form.

We have also a footer in all pages where we have only a copyright statement. There is not option to contact ot loging in this 
initial idea of the project. 

### Home
Shows basic sustainable principies of the Green Construction, with different images/icones/text. 
This a landing page base on Themes from startbootstrap.com

### Green Builders Community Gallery
Displays all the records of the Comunity. It is also possible to filter by category based on main materail used 
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

We have 3 buttons:
* Delete: On click we will get and alarm with text 
*This process cannot be undone! Are you sure you want to delete this house?*. 
 And options to continue or cancel the operation.

* Home: To navigate to the Welcome page.

* Edit: On click it will open a new page, Edit Green Building page.

### Edit Green Building
Displays a Form with select option and filds to fill in requested details.
Using Materializecss.com

We will find 2 buttons:
* Update: This button must be clicked to save the changes of the records.
* Cancel: If we click on cancel, we will get and alert with the next message: 
  *Your building has not been edited.*

### Add your own
This is similar to the Form at Edit Green Building page.
In this case we must fill in also required filds and at the end we will find different buttons to:
* Insert: On click add the records to the data base of the Comunity. And drives you to View More Details page 
  where you can Delete or Edit the inserted data.
* Cancel: On click it will cancel the operation and nothig will be added to the data base.

Visiting Green Builders Community Gallery, we will see that the new record is displayed at the end of the list. 
Or if you select a category it will displayed at the end of the records under that caterory.

## Features to add in future
Add a Sign In/Sign Up option to cretae a real feeling of membership.
Restrictions to Edit or Delete base on membership.
Chat for the members to communicate between them. 

## Existing features
Navigation bar - Collapsible for small screens.
CRUD - Users can upload, read, update, and delete content in the database
Sorting - Users can sort through keyboards

## Technologies used

This Green Building web application was built using different languages:
**HTML5**, **CSS3**, **JavaScript** was used to build an interactive webpage.
And **Python** was used to build the structure and functionality of the back end.

### Libraries to style interactive options:
**Bootstrap CSS**
**Bootstrap JS**
**FontAwesome**
**jQuery**
**Dnspython**
To make the structure and the site responsive in a simple manner **Materialize** 
were used for Nav, Forms and select.
**Flask** was used to display python functions on the website.
**Pymongo** was used to make the code written in python talk to the database.

### Tools:
**MongoDB** was used as the database host.

### Deployment/Host:
**Heroku** was used to deploy the live version of the application.
The website is built and developed using **GitPod** as IDE.

### Testing:
**W3C's HTLM Validator** 
**W3C's CSS Validator** 
**Responsinator**

## Deployment
GitPod was used as IDE to develop this application. Throug out the development, the project was 
commited to the git and continuously pushed to Heroku connected to GitHub. 

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

**W3C's HTLM Validator** were used to validate the websites HTML code.

**W3C's CSS Validator** were used to validate the websites CSS code.

**Responsinator** used to check responsiveness.

Pages work as expected in a responsive manner. All select options, forms and buttons tested. 
Only a function to clear the selected categories in the dropdown is yet to be implemented. 
When the user clears the filters and are beeing displayed with all options the previously 
selected options in the dropdown remains unchanged. Clear the dropdowns fintcion must be implemented in future.

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










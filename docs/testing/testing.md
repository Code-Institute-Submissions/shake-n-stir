# Testing

Table of Contents?


I have organized the testing.md file by first testing the HTML files, CSS file, the JavaScript file, the Python file, and finally general site testing. I tested each component of the website on desktop, tablet, and mobile. 

## HTML 

I passed all HTML code through the W3C Markup Validation Service. I recieved two errors, which are outlined below: 

1. I had an error on the cocktails.html page due to duplicate ids. These duplicate ids referred to the search functionality which is used twive on this page (once in the footer and once at the top of the page). This error was quickly fixed by changing the id.

2. For the categories.html page, I received an error for having a div(modal) inside of a 'ul'. If I moved the modal outside of the ul, it would no longer target the correct categories. However, a div is allowed to be placed within a 'li' and once placed here, the error no longer appeared. 

I passed all pages through the W3C Markup Validation Service again, and no errors were found. 

## CSS

I tested my CSS code via W3C CSS Validator. No errors were found here. 


## JavaScript 


### JSHint Testing 

I passed the script.js code through JSHint to see if there were any errors or warnings.  

No errors were found. 

I received a warning message regarding an undefined variable 'cloudinary'.

As this variable was related to the cloudinary widget, I chose to ignore this warning, as it is needed to initialize the Cloudinary widget. 

I received a warning message regarding an unused variable 'validation'. I have also chosen to ignore this message as this variable is part of Bootstrap's validation script. 


### General JavaScript Testing

I have mainly used JavaScript to help add and remove classes for validation purposes on the login and register form. 

1. I submitted a form with all fields empty and confirmed that the invalid class was activated. 

2. I tried to make a new user account, and intentionally used two different passwords for the password, and confirm password field. I confirmed that the confirm password field displayed the invalid feedback text and displayed a red border. 

3. I ensured that the password and confirm password fields matched, and confirmed that the invalid feedback text vanished, and the class valid was added, allowing users to proceed. 

4. I clicked on the cloudinary widget button and confirmed the widget has opened as expected. I selected a file and successfully attached it to a cocktail. 

5. In general, if there is an image URL in the upload image input field, and a user clicks the Cloudinary widget button, it won't open as there is already a value in the field. I have created a script to remove the input field value when the cloudinary widget is clicked. To test, I pasted an initial image URL in the field. I then clicked the Cloudinary widget button and confirmed the previous value had been removed, and it was possible to upload a different image. 

6. When using the edit cocktail form, I uploaded a new image and confirmed that the thumbnail preview of the previous image has been removed, and replaced with the newly uploaded image. 

7. I hovered over each cocktail card, and confirmed that when hovered it created a box-shadow effect. 


## Python

I tested my Python code using [PEP8 Online Validator](http://pep8online.com/). There were no errors found.

I checked Gitpods python linter, and no errors were found, except for the env, WHICH I'LL REMOVE WHEN COMPLETE!

## Site General Testing

I tested the various aspects of the website through the development process. Once the project was deployed to Heroku I once again tested the website, to ensure that there were no oversights or unknown bugs. 

### Navigation

#### Navbar

* I clicked on the navigation link 'Home' and confirmed it returns to the home page. 
* I clicked on the navigation link 'Cocktails' and confirmed it takes the user to the relevant page. 
* I clicked on the navigation link 'Register' and confirmed it leads the user to the registration form. 
* I clicked on the navigation link 'Login' and confirmed it takes the user to the login form. 
* I finally clicked the navbar brand and confirms it redirects the user back to the home page. 
* I logged into the admin account, clicked on the link 'Categories', and confirmed that it redirects to the Category page. 
* I checked once a user creates an account, Log in and Register nav links disappear, and the profile button appears. 
* I clicked on the profile dropdown button, to ensure it was working correctly. 
* I clicked on the profile button and clicked on the Add Cocktail nav link, to confirm it leads the user to the Add Cocktail page. 
* From within the profile dropdown menu, I clicked on the Profile nav link and confirmed that it directed users to their profile. 
* I clicked on the log-out link from the dropdown menu and confirmed that it logs the user out.
* I hovered over each nav link to confirm that the hover effect is working correctly. 
* I tested the navigation on mobile and tablet and confirmed the hamburger icon works correctly and opens the navigation menu. 


#### Footer 

* I clicked on each social media icon in the footer and confirmed that it directed users to a new tab with the correct website opening.
* I clicked on each section of the site map in the footer to confirm it re-directed the user to the correct section. 
* I entered a cocktail name in the footer search bar and confirmed it directs users to the cocktail page with the relevant cocktail showing. 
* I entered a cocktail name that did not exist and confirmed that the results page stated 'No Results Found', and displayed a list of popular cocktails. 
* I confirmed that on mobile, the footer links are stacked to aid with design. 


### Further General Testing on Homepage. 

* I clicked on every home page button to make sure that they led the user to the correct section of the website. 
* I clicked on the cocktail cards featured on the home page and confirmed they directed users to the correct cocktail page. 

### Registration and Login Functionality 

#### Register Form

* I created an account for a user with a correct username and password and confirmed the account was created successfully. I checked the database and could see the newly created user.
* I attempted to create an account with a username that already exists in the database. I confirmed it is not possible, and the user is notified the username already exists. 
* I attempted to create an account without matching the password fields and confirmed both password fields need to match to create an account. 


#### Login Form

* I inputted the correct username and password for an account and confirmed it logged a user in successfully. 
* I inputted an incorrect username and correct password and confirmed a user is unable to log in without correct credentials. 
* I attempted to log in with a correct username and incorrect password and confirmed that a user is unable to log in without both fields being correct. 

### User Profile Functionality 

* I confirmed that once a user logs in or creates an account, the user profile renders their created cocktails and not other user-created cocktails. 

* I have also tried pasting another user's username into the profile URL field and confirmed that it did not render another user's profile. A profile function will only render the current user's account. 

* I clicked the log out button and confirmed that the log out function works correctly, and removes the current user from the session.  

* I used both the browser navigation buttons and pasting the URL to go back to the user profile page without a user logged in, I can confirm that it correctly redirects to the login.html page. 

* I deleted a user profile and confirmed that it had been removed from the database. 


### Cocktail Collection Page

* I confirmed that all cocktail cards loaded their images correctly.
* I confirmed each cocktail card directed users to the correct cocktail page, by clicking on the view button, and also testing again by clicking on the cocktail card anchor tag Title. 
* I ensured that all text was easily readable to users. 
* I hovered over the cocktail cards to ensure the box-shadow is triggered.


### Individual Cocktail Page

* I confirmed that the list of group items was correctly populated. 
* I confirmed that all icons were correctly placed alongside their relevant titles. 
* I logged into an account that had not created a cocktail and confirmed such users are unable to see the Edit and Delete buttons. 
* I logged into an account that created a cocktail and confirmed that the Edit and Delete buttons appear for the relevant user. 
* I checked to ensure that the edit button takes a user to the Edit Cocktail form with correct cocktail information, referring to the correct cocktail ID. 
* I clicked the delete cocktail button and confirmed that it triggers a modal, to confirm the deletion.
* I have also deleted a cocktail and confirmed it correctly deletes the targetted cocktail. 
* I have also confirmed that the Edit Cocktail form populates with the relevant information for the specific cocktail ID. 
* I removed required inputs from the Edit Cocktail form and confirmed that the form will not submit if the form is not validated. 
* I removed the image from the image URL field, and confirm that the thumbnail preview vanishes. 
* I inputted a new image and confirmed that a new thumbnail preview populates.

### Add Cocktail Page

* I tried to submit an empty cocktail form and confirm that required fields prevent the form from being submitted without the correct input. 
* I tried to submit the cocktail form with the incorrect information, for example, adding a letter to the Cocktail Serving field. I confirmed that the user is prompted with a feedback message, and the form doesn't submit. 
* I created an error for each field and confirmed that all invalid feedback messages populate. 
* I clicked on the Cloudinary widget button to confirm that it opens the widget to allow for users to attach an image. 
* I placed an image URL directly into the Upload Image field and confirmed that it accepts the image URL. 
* I confirmed that by clicking the widget initializer that the image input field is cleared to allow for a new image to be submitted. 
* I submitted the cocktail form with correct information and confirmed that the cocktail was submitted successfully, and populated on the cocktails.html page. 

### Search Functionality

* I searched for a created cocktail and confirmed that the relevant cocktail populated in the search results. 
* I searched for each cocktail category and confirmed that all relevant cocktails populated in the search results. 
* I have searched for cocktails, and categories that do not exist, and confirmed that the correct information is displayed. Namely; 'No Results Found', a button that links users back to viewing all cocktails, and a list of popular cocktails. 


### Category Page

* I confirmed that the Category page is not visible or accessible to users without the correct credentials. 
* I have confirmed that all Categories are present. 
* I clicked on the edit category button and confirmed it leads to the correct page with the correct category information. 
* I tried to submit a new category both from the edit category form, and add category form, with an empty input, however, the form is prevented from being submitted. 
* I clicked on the delete category button and confirmed that the modal confirmation is triggered.
* I clicked on the modal delete button and confirmed that the category is removed from the database. 
* I correctly submitted the Add Category form, and confirmed it populated on the category page, and category section in add/edit cocktail forms.


### 404 Page 

* I entered an incorrect URL and confirmed that the 404.html is rendered. I confirmed that the home button on the 404 page redirects users back to the correct page.
* I have confirmed that the navigation links and footer links operate correctly on the 404.html. 


### Responsiveness 

* I tested the responsiveness of the website across all three major devices; desktop, tablet, and mobile phone. The website keeps the correct structure. 

* I tested the website across several browsers, with no issues to report. The browsers tested are Google Chrome, Firefox, and Safari.

* I tested the website using [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) and the website has passed. 

* I tested the website uisng Google Lighthouse on both mobile and desktop. The website scored '97' on Desktop and '81' on Mobile.


## Testing User Stories 


* I want a website that allows me to create my cocktail recipes.
    * This is evident in the Add Cocktail form, which allows a user to create their cocktail. 
        * You can see this [here](./user-stories/user-story-add-cocktail.png)

* I want a website where I can view other people's cocktail recipes. 
     * This is evident in Cocktail Collection, which allows a user to view all cocktails created by other users.
        * You can see this [here](./user-stories/user-story-view-other-cocktails.png)

* I want the ability to search for cocktails on the website. 
    * This is evident from the Cocktail Collection page where a user can search for specific cocktails. This is also evident in the footer where there is a search function, that users can utilize on any page. 
        * You can see this [here](./user-stories/user-story-search-cocktails.png)
        
* I want a website that is easily accessed on my mobile phone and tablet. 
     * The website is responsive for both mobile phones and tablets. I have taken steps to ensure each device is a smooth experience. I have achieved this by adhering to bootstrap's responsive classes as well as custom media queries used throughout the website. 
        * You can see this [here](./user-stories/user-story-mobile-view.png)

    * The navigation bar also changes to a hamburger-style icon on smaller devices. The dropdown navigation bar frees up screen space on mobile and tablet devices.
        * You can see this [here](./user-stories/user-story-smaller-nav.png)
    * The amount of cards showing on a row is also adjusted depending on the size of the user's device. On mobiles, a card takes up one row, whereas, on a desktop, there are three cards. 
        * You can see this [here](./user-stories/user-story-mobile-view.png)

* I want a website that is easy to understand and navigate. 

    * The hero image, and jumbotron quickly outline the main purpose of the website. I have developed the website to be easily understood, and easy to traversable. This is achieved by utilizing visual cues such as buttons, icons, and relevant navigation links. 
    * Each navigation link is clearly stated and directs users to the relevant sections.
        * You can see this [here](./user-stories/user-story-nav-bar.png) 
    * All social media links are clearly outlined, and when clicked, open a new tab. 
    * All navigation links display a subtle hover effect to provide a visual cue to a user what they are about to click.
    * I have also opted to use hover effects on buttons, which often change color when hovered, which displays to the user what they are about to click. 
    * All forms are outlined, and provide guidelines via placeholders and invalid feedback
        * You can see this [here](./user-stories/user-story-helper-text.png)

* I want to have my own profile to store my created cocktails.

    * When a user creates a cocktail, the cocktail information is also stored on their profile. Each time a user is logged into their Profile, they can quickly view their cocktails. 
        * This can be seen[here](./user-stories/user-story-view-self-cocktails.png)

* I want to be able to edit or delete my created cocktail recipes.

     * If a user has created a cocktail, they are given the option to edit and delete their cocktail. This can be accessed from the main cocktail page, or from a user's profile.

        * Examples of editing and delete options from a user's profile can be seen [here](./user-stories/user-story-edit-delete.png)

* I would like to be able to follow the website's social media accounts.

    * The social media accounts for the website are displayed on every page in the footer section. Once a user clicks on a social media icon, a new tab is opened and directs users to the relevant social media page. 
        * The social media icons can be viewed [here](./user-stories/user-story-social-media.png) 

* I want my profile to be password protected.

    * A user is not able to create an account, without also creating a password for their account. A profile cannot be accessed when logging in without knowing the password. In addition, all passwords are protected by hashing. 
        * A the login form displaying the password can be seen [here](./user-stories/user-story-password.png)

# Whiskey Drop (Deluxe)

Fourth Milestone Project for the Web Development course offered by Code Institute. A site for purchasing quality whiskey.

## Table of Contents
1. [UX](#ux)
	- [Project Goals](#project-goals)
	- [User Goals](#user-goals)
	- [User Stories](#user-stories)
	- [Design Choices](#design-choices)
2. [Planning](#planning)
	- [Wireframes](#wireframes)
 	- [Schema](#schema)
3. [Future Additions](#future-additions)
4. [Testing](#testing)
	- [User Stories Testing](#user-stories-testing)
 	- [Bugfixes](#bugfixes)
5. [Technologies Used](#technologies-used)
6. [Deployment](#deployment)
7. [Credit](#credit)

## UX

### Project Goals

Whiskey Drop

### User Goals

- Simple design.
- Visually appealing.
- Easy to navigate.

### User Stories

- As a user, I want ?
- As a user, I want ?
- As a user, I want ?
- As a user, I want ?
- As a user, I want ?
- As a user, I want ?

### Design Choices

#### Interface

Pending.

## Planning

### Wireframes
Pending.

### Schema
Pending.

## Testing

<!-- The site has been tested extensively to ensure the best user experience across multiple screen sizes.

The developer used **W3C CSS Validation Service** and **W3C Markup Validation Service** to check the validity of the HTML and CSS. -->

### Testing Process
<!-- 
To make sure the site renders acceptably across several screen sizes, I made liberal use of the DevTools offered by Google Chrome, as well as testing load times, mobile and desktop, with the Lighthouse Chrome extension.

![Testing main page desktop version.](docs/lighthouse-test-desktop.png)

![Testing main page mobile version.](docs/lighthouse-test-mobile.png) -->

### User Stories Testing

As a user of the site, I want:
- ?
	- ?
 	- ?
- ?
	- ?
 	- ?
- ?
	- ?
 	- ?
- ?
	- ?
 	- ?
- ?
	- ?
 	- ?

### Bugfixes
- Problem: The top of the product details pages were covered by the navbar.
	- Solution: Added padding to the `heading-container` in `base.css` to account for this, and adjusted the `body` to compensate.
- Problem: The `quantity_input_script` I added to `product_detail` wasn't working - pressing either the + or - button just added directly to the cart.
	- Solution: I hadn't added a `{% block postloadjs %}` to my `base.html`, which is where the `quantity_input_script` was located. Adding the postloadjs block immediately fixed the issue.
- Problem: I could not adjust items in the cart or remove them from the cart.
	- Solution: I was missing a few key adjustments to my code (using the slim version of jQuery instead of the normal version, using `url adjust_cart` instead of `url 'adjust_cart'`, not adding a `/` to the end of the JavaScript and so on). After fixing all of these small issues, I was able to adjust and remove items from the cart without issue.

## Technologies Used

### Building
- [HTML5](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS53](https://developer.mozilla.org/en-US/docs/Learn/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Python](https://docs.python.org/3/)
    - [Django](https://docs.djangoproject.com/en/5.0/)
- [PostgreSQL](https://www.postgresql.org/docs/)

<!-- ### Testing
- [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)

### Validation
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) -->

## Deployment
Deploy to Heroku or a similar website hosting and rendering service. The html files can also be opened from local storage (this requires downloading all files in a dedicated folder; this can be done with the git pull command), though the pages won't properly work without the Python code added.

<!-- To deploy this site to Heroku from [its GitHub repository](https://github.com/cosmicCode42/OC-archive), the following steps were taken.

1. Log in to a PostgreSQL database service.
2. Create a new PostgreSQL database. On Aiven, this is done by creating a new service. You must create a project beforehand, then add the service inside that project.
3. Copy the database URL (service URI on Aiven).
4. Make sure to create a `requirements.txt` file with the terminal command `pip freeze --local > requirements.txt`. Make sure to save the file and add, commit and push it to your repository. (Unnecessary here since this project already has a requirements.txt file.)
5. Make sure to create a Procfile and add the command `web: python run.py1` into it. Make sure to save the file and add, commit and push it to your repository. (Unnecessary here since this project already has a Procfile.)
6. Your `__init__.py` file will require a few lines of code (my `__init__.py` already has these so if copying mine this can be safely ignored). Refer to [oc-archive-troubleshoot](oc-archive-troubleshoot.txt) for the exact code.
Make sure to save the file and add, commit and push it to your repository.
8. Log in to [Heroku](https://www.heroku.com/).
9. Create a new app.
10. Go to the Settings of your app and click Reveal Config Vars. Add your copied database URL as `DATABASE_URL`, then add each of the other environmental variables: `DEBUG` (`True` or `False` depending on the current state of the project), `IP` (usually set to `0.0.0.0`), `PORT` (usually `5000`), `SECRET_KEY` (you make a unique one).
11. Go to the Deploy tab of your app. In the Deployment method section, select "Connect to GitHub". You can click "Enable Automatic Deploys" so that each time you commit to your GitHub repository, the Heroku app is redeployed.
12. Click the "More" button next to "Open App" and select "Run console". Run `python3` in the Heroku console. -->

<!-- If the steps are followed correctly, when opening the app, the website should be fully functional. The new database will be empty, so you will have to add new users -->

At the moment of submitting the milestone project, the development branch and main branch are identical.

### How to run the project locally

To clone this project from GitHub:

1. Follow this link to [its GitHub repository](https://github.com/cosmicCode42/whiskey-drop-dx).
2. Under the Code dropdown menu in the Code section, you can copy the HTTPS link or download a ZIP.
3. A copied link can be used to make a pull request using Git Bash. 
	1. Change the current working directory to one where you want the clone to be made.
	2. Run ``git init`` to initialise a local repository.
	3. Run ``git remote add origin`` and paste the copied link right after. Running this command sets the GitHub repository as the 'origin'.
	4. Run ``git branch -M main`` if the local repository doesn't have a main branch.
	5. Run ``git pull origin main`` to make the pull request.

### Cloning project into GitPod

To clone this project into GitPod, you will need:
- A [GitHub](https://github.com) account.
- A Chrome browser or compatible browser.

Then follow these steps:
1. Install the [GitPod browser extension for Chrome](https://www.gitpod.io/docs/configure/user-settings/browser-extension).
2. Restart the browser after installation.
3. Log into [GitPod](https://www.gitpod.io) with your GitHub account.
4. Navigate into the [Project GitHub repository](https://github.com/cosmicCode42/whiskey-drop-dx).
5. Click the green **GitPod** button in the top right corner of the repository. This will trigger a new GitPod workspace to be created from the code in GitHub where you can work normally.

## Credit

### Code

Code not written by me and not covered below is attributed to proper sources in comments within the code. All other code is written by me.

#### Guidance and Inspiration

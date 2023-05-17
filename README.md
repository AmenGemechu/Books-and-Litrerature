# Books & Litrature Quiz
Deployed Site: https://books-and-literature-quiz.herokuapp.com/

![B LQ](https://github.com/AmenGemechu/Portofolio-3/assets/81637641/56526e90-31a2-4af9-a1c3-cc026d473635)


Books & Literature Quiz is a command-line application built with Python, where users can test their knowledge of Books & Litrature and learn interesting fun-facts about the subject.
Users of the application will be asked several questions and their score is kept track of throughout the game. Once the game is completed, score will be calculated by a percentage and displayed to player.
At the end ofthe game users will have the choice of replaying if they wish to.
User score will be saved and will be added to their previous score every time they play. 

* [UX](#user-experience)
    * [Flowchart](#target-audience)
    * [User stories](#user-stories)
    
*  [Technologies](#technologies)
   * [Languages](#languages-used)
   * [Libraries](#libraries)

* [Testing](#testing)
    * [Manual Testing](#manual-testing)
    
* [Bugs](#bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)

* [Deployment](#deployment)
   * [Herocku Deployment](#heroku-deployment)

* [Credits](#credits)
    * [Acknowledgments](#acknowledgments)


# UX
## Flowchart
![Books   Litrature Quiz - Page 1](https://user-images.githubusercontent.com/81637641/235639386-208eb6d2-a0cf-4fdb-a5f1-1216cf545bd0.jpeg)


## User Stories

    As a user, I want to see the logo and welcome message.
    As a user, I want to see instructions on how the quiz works.
    As a user, I want to create my user name.
    As a user, I want to see the question and multiple-choice options.
    As a user, I want to see wether my answers were correct or incorrect.
    As a user, I want to see my score.
    As a user, I want to be able to replay.
    As a user, I want my score to be saved
    As a user everytime i replay, i want my score to keep being added to my previous scores.
    As a user i want to see my answers.


# Technologies
## Languages
- Python
## Libraries
- Git
- GitHub
- pip8
- Heroku
- Lucidchart

# Testing
- Testing was done using PEP8
    - there were no errors found
![PEP8](https://github.com/AmenGemechu/Portofolio-3/assets/81637641/1f56605e-32e8-4f61-8ce4-ce98a080fc4e)

# Bugs
## Fixed Bugs
- branch and 'origin/main' have diverged due to different commits. Issue was resolved by using "git pull" to merge the remote branch with main branch.
- play_again function 
    - try/excep: break as causing while loop to exit early.
    - fixed bug by replacing it by if/else. 
## Unfixed Bugs
- None

# Deployment
## Herocku Deployment
   1. Create an account at Heroku and login.
   2. Click the "Create new app" button on your dashboard, add app name and region.
   3. Click on the "Create app" button.
   4. Click on the "Settings" tab.
   5. Under "Config Vars" click "Reveal Config Vars" add your credentials as value with "CREDS" as key.
   6. Under "Buildpacks" click "Add buildpack" and then choose "Python" first and click "Save changes"
   7. Add a second buildpack "nodejs" and click "Save changes"
   8. Go to the "Deploy" tab and choose GitHub as your deployment method
   9. Connect your GitHub account
   10. Enter your repository name, search for it and click connect when it appears below.
   11. In the manual deploy section click "Deploy branch"
   12. Optional: You can enable automatic deploys if you want the app to automatically update

# Credits & Acknowledgments
- Logo text was made using 
https://textkool.com/
- Type_writer effect code was taken from:
    https://stackoverflow.com/questions/20302331/typing-effect-in-python
- Questions were taken from
    https://keepingupwiththepenguins.com/trivia-questions-about-books-and-literature-answered/


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# dft-contacts

Django application created for a job application. The original brief is at the bottom of this README.

This app was created using Python 3 and the instructions give Linux commands. However, the repo ought to run on Windows, too.

## Setup

Clone the repo locally using `git clone url/copied/from/github`.

Create a virtual environment using the command `py -m venv venv`. Then open your virtual environment.

Install any packages using `pip install`. _**[ENSURE THAT THE FILE CONTAINING ALL PACKAGE INFO IS IN THE REPO AND UP TO DATE. USE `pip freeze`]**_

To seed the SQLite database, open `dft_contacts/seed_script.py` and follow the instructions in the comment at the top. This will give you a few dummy users to play around with.

## Data storage

We are using the out-of-the-box SQLite feature that Django provides. At present, the database has only one table, which uses the `Contact` model.

## Deploying to production

Django is cross-platform and can be run from any major hosting provider. My preference is Azure, mainly because I use it for work, but also for their excellent setup guides. They have a very good [one for Python apps](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cazure-cli-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli#create-a-web-app-in-azure).

Azure's automated system will handle the installation for you.

To seed the database with dummy data (not normally necessary in production), you will need to access the Azure command line to interact directly with your repo, following the instructions given above.

## Brief

Develop a simple Contacts web application that stores information such as name, address, and telephone numbers for contacts. Users should be able to see a list of contacts, as well as be able to perform CRUD activity for contacts.

This application should:

- Demonstrate your ability to build a basic web application.
- Showcase your proficiency with web development frameworks and tools.

### Requirements

- Use any web application framework to complete this task. Python frameworks such as Django are recommended, but any language and framework are acceptable. The focus is on demonstrating proficiency.
- **Front-End:** Develop a basic web front-end to interact with the application. Apply some styling to create a visually appealing interface.
- **Data Storage:** Store contact information in a database. SQLite is suggested for simplicity, but other databases or data storage solutions (e.g., JSON files) are acceptable.
- **API:** Provide a basic API that serves the application’s data.
- **Dynamic Interactions:** Include a few examples of dynamic user interfaces, such as AJAX interactions or partial updates to the DOM. These are considered as extra features but will showcase your ability to enhance user experiences.
- **Local Environment:** The application only needs to run on a local machine and does not need to be deployed as a live site.
- **Version Control:** Use Git for version control. Publish the code repository to an open-source platform such as GitHub or an equivalent service.
- **Documentation:** Include a README file with:
  - Instructions for cloning the repository.
  - Steps to install dependencies.
  - Guidelines to run the application locally.
  - High-level instructions on deploying the application to production, including a recommended cloud platform and service (e.g., AWS, GCP, Azure).

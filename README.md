# dft-contacts

Django application created for a job application. The original brief is at the bottom of this README.

This app was created using Python 3 and the instructions give Linux commands. However, the repo ought to run on Windows, too.

## Setup

Clone the repo locally using `git clone url/copied/from/github`.

Create a virtual environment using the command `py -m venv venv`. Then open your virtual environment.

Install any packages using `pip install`. _**[ENSURE THAT THE FILE CONTAINING ALL PACKAGE INFO IS IN THE REPO AND UP TO DATE. USE `pip freeze`]**_

## Data storage

For the time being, data is being stored in JSON format, like so:

```json
{
 "types": [ "array", "of", "contact", "types", "e.g.", "friends", "family", "other" ],
 "contacts": {
  "id1": {
   "first_name": "John",
   "last_name": "Doe",
   "email": "john@doe.com",
   "mobile": "07111 111 111",
   "types": [ "family" ]
  },
  "id2": "..."
 }
}
```

The `contacts` object contains a dictionary of `contact` objects whose key is their user ID.

In a NoSQL database, the `contact.types` would contain references to the top-level `types` array.

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

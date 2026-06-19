Business Context
In the realm of travel and tourism, the intersection of data analytics and machine learning presents an opportunity to revolutionize the way travel experiences are curated and delivered. This capstone project revolves around a trio of datasets - users, flights, and hotels - each providing a unique perspective on travel patterns and preferences. The goal is to leverage these datasets to build and deploy sophisticated machine learning models, serving a dual purpose: enhancing predictive capabilities in travel-related decision-making and mastering the art of MLOps through hands-on application.

Brief overview of each datasets
Users Dataset:

code: User identifier.

company: Associated company.

name: Name of the user.

gender: Gender of the user.

age: Age of the user.

Flights Dataset:

travelCode: Identifier for the travel.

userCode: User identifier(linked to the Users dataset)

from: Origin of the flight.

to: Destination of the flight.

flightType: Type of flight (e.g., first class).

price: Price of the flight.

time: Flight duration.

distance: Distance of the flight.

agency: Flight agency.

date: Date of the flight.

Hotels Dataset:

travelCode: Identifier for the travel, similar to the Flights dataset.

userCode: User identifier(linked to the Users dataset)

name: Name of the hotel.

place: Location of the hotel.

days: Number of days of the hotel stay.

price: Price per day.

total: Total price for the stay.

date: Date of the hotel booking.

Project Objectives
1. Regression Model Development:

Build a regression model to predict the price of a flight using the flights.csv dataset. Focus on feature selection, model training, and validation to ensure accuracy and reliability.

2. REST API for Regression Model:

Develop a REST API using Flask to serve the flight price prediction model, enabling real-time price predictions.

3. Containerization:

Package and deploy the flight price prediction model using Docker, ensuring portability and ease of deployment.

4. Kubernetes for Scalability:

Deploy the model using Kubernetes to manage scalability and handle varying loads efficiently.

5. Automated Workflows with Apache Airflow:

Design and implement automated workflows for managing the travel data, specifically for the regression models. Develop Directed Acyclic Graphs (DAGs) to orchestrate complex workflows in an efficient and manageable way.

6. CI/CD Pipeline with Jenkins:

Implement a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Jenkins for consistent and reliable deployment of the travel price prediction model.

7. Model Tracking with MLFlow:

Utilize MLFlow for tracking and managing different versions of the travel price prediction model, ensuring a systematic approach to model iteration and deployment.

8. Gender Classification Model:

Deploy a classification model to categorize a user's gender.

9. Travel Recommendation Model:

Build a recommendation model to provide hotel suggestions based on user preferences and historical data. Develop a Streamlit web application to display insights and visualizations derived from the deployed travel recommendation model, offering an interactive and user-friendly interface for data exploration.

1. Technical Accuracy and Implementation (40%)

Accuracy of the regression, classification, and recommendation models.
Correct implementation of REST API, Docker, Kubernetes, Apache Airflow, and Jenkins.
Effective use of MLFlow for model tracking.
Functionality of the Streamlit web app.
2. Code Quality and Documentation (15%)

Readability and organization of code.
Adequate commenting and clear code documentation.
Comprehensive README files and user guides for each component.
3. GitHub Structure, Commits, and README (10%)

Organized GitHub repository structure, with clear separation of components (e.g., models, API, Docker, etc.).
Meaningful commit messages reflecting the development process and incremental changes.
Comprehensive and well-structured README file in the GitHub repository, detailing project overview, setup instructions, usage, and other relevant information.
4. Model Performance and Evaluation (5%)

Appropriate metrics used for evaluating the models.
Performance of models based on these metrics (e.g., accuracy, precision, recall, RMSE).
In-depth analysis and interpretation of model results.
5. MLOps Integration and Workflow Automation (10%)

Smooth integration of MLOps practices.
Efficiency and reliability of automated workflows with Apache Airflow.
Effective use of CI/CD pipeline in automating the model deployment process.
6. Presentation and Reporting (20%)

Clarity and professionalism in the presentation of the project.
Fluency and Grammatical Accuracy in the Video
Coherence and comprehensiveness of the final report and documentation.

Files that must be submitted
Individual Collab Notebook with the pre-defined Project template format for regression, classification and recommender modeling part. Include well-explained and reasoning paragraphs (with the Project Summary & GitHub Repo link inside)
There should be only one GitHub link under a single repo which should contain all the files related to the whole MLOps process - pickle/joblib, flask app, streamlit app, docker file, requirements.txt, deployment.yml, dag files, mlflow code etc.
Separate documentation in Google Doc explaining the workflow for each of the stages in MLOps with screenshots- REST API, Streamlit App, Docker Deployment, Kubernetes Deployment, Scheduling in Airflow, CI/CD Pipeline and MLFlow Tracking.
(Notes:-

Don't write the installation process of any tool in the documentation.
The Flask API could be made in colab or a local code editor)
A Video presentation explaining the whole process from modeling-deployment-scaling-scheduling-pipelining-monitoring. Explain only for the regression model. Explain the important components and stages in each part. (Minimum 40 mins.)
Ensure the explanation video lasts no less than 15 minutes.
File Sharing and Uploading Options
Upload all the 3 colab files, separate doc files in Google Drive and submit the drive link under Project link, while the presentation link under Video link in submission dashboard.
The work and the submission should be completely individual.
Make the google collab file accessible (view) to everyone.
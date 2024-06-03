### Problem Statement: Deploying a Scalable ML-Powered Ads Conversion Prediction System

#### Background

In the highly competitive digital advertising space, understanding and predicting user behavior is critical to maximizing conversion rates. Businesses invest significantly in ads, aiming to convert views into actions, such as purchases or sign-ups. However, predicting conversion rates accurately is a complex challenge due to the myriad of factors influencing user behavior, including demographics, engagement metrics, and online activity patterns.

#### Objective

The objective of this project is to develop and deploy a scalable machine learning-powered system that predicts ad conversion rates based on user data. The system will be built using a Flask web application, incorporating a pre-trained machine learning model. It will be containerized using Docker and deployed on AWS infrastructure to ensure scalability, reliability, and ease of maintenance.

#### Key Components

1. *Machine Learning Model*: A pre-trained machine learning model capable of predicting ad conversion rates based on features such as age, gender, location, language, educational level, income level, device usage, time spent online, likes and reactions, followed accounts, click-through rates, and ad interaction time.

2. *Flask Web Application*: A web interface allowing users to input relevant data and receive predictions on ad conversion rates. The application will include both the user interface (HTML/CSS) and backend logic (Python/Flask).

3. *Containerization with Docker*: The entire application, including the machine learning model and Flask web server, will be containerized using Docker. This ensures consistency across different environments and simplifies deployment.

4. *AWS Deployment*: The Docker container will be deployed on Amazon Web Services (AWS) using Elastic Container Service (ECS) and Elastic Container Registry (ECR). AWS will provide the necessary infrastructure to handle varying loads, ensuring the application is both scalable and reliable.

#### Challenges

1. *Integration and Deployment*: Integrating the machine learning model with the Flask application and ensuring smooth operation within a Docker container.
2. *Scalability*: Deploying the application in a manner that supports auto-scaling to handle high traffic loads efficiently.
3. *Reliability*: Ensuring the system is robust and can recover gracefully from failures or unexpected spikes in usage.
4. *Security*: Protecting user data and ensuring the application is secure from common web vulnerabilities and attacks.

#### Expected Outcomes

1. *Functional Web Application*: A user-friendly web application that allows users to input data and receive accurate ad conversion predictions.
2. *Scalable and Reliable Deployment*: A fully containerized application deployed on AWS, capable of handling increased loads and ensuring high availability.
3. *Documentation and Best Practices*: Comprehensive documentation outlining the development, containerization, and deployment processes, adhering to MLOps best practices.

#### Impact

By deploying this system, businesses will gain a powerful tool to predict and optimize ad conversion rates, leading to more effective advertising strategies and higher return on investment (ROI). The use of AWS infrastructure ensures the system can scale seamlessly to meet demand, providing a robust and reliable solution for digital marketers.


### Steps Performed for Predictions:

1. Data Ingestion:	Firstly, the data is loaded and ingested from the file and split into training and testing sets.
2. Data Engineering:    The categorical features are classified into two types: Ordinal and Nominal. A pipeline of feature transformation is created and a pickle object is created for the same which involves the following:
a. Ordinal Variables are encoded using Ordinal Encoder and imputed using SimpleImputer with mode value
b. Nominal Variables are encoded using OneHotEncoder and imputed like the ordinal variables.
c. Numerical Variables are scaled using StandardScaler and imputed with mean value.
3. Model Training: 	Different models like SVR, Linear Regression, Random Forest Regressor and KNN Regressor are trained by the model_training program and the model with the best score is chosen by the same. It is then re-trained and another pickle object is created for the same.
4. Predictions:		The form input data is first converted into a Pandas DataFrame. It is then transformed with the help of preprocessor pickle object and predicted using model pickle object.

### Output: 

![Input](https://github.com/202318012/CTR/Screenshot (264).png)
![Input](https://github.com/202318012/CTR/Screenshot (266).png)
![Output](https://github.com/202318012/CTR/Screenshot (267).png)

### Conclusion

This project demonstrates a comprehensive approach to developing and deploying a machine learning-powered prediction system using modern MLOps practices. It highlights the integration of machine learning models with web applications, containerization for consistency, and leveraging cloud infrastructure for scalability and reliability. Through this project, businesses can harness the power of machine learning to make data-driven decisions and enhance their advertising strategies.



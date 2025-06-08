Project Report: Predicting House Prices Using Machine Learning
Institution: Eastern Africa Statistical Training Centre
Program: Bachelor Degree in Data Science
Abstract
This project explores the application of machine learning in real estate price prediction, focusing on urban areas of Tanzania. The system is implemented as a web-based application using Django, integrating machine learning models trained on housing datasets to estimate property values based on structural features, location, and year built. The project delivers a secure, user-friendly web interface where users can register, log in, and predict house prices. It also includes administrative features, password reset options, and currency conversion. The end goal is to provide a scalable decision-support tool for buyers, sellers, agents, and analysts in the housing market.
1. Introduction
Background
House price estimation is a complex problem influenced by multiple variables such as location, number of rooms, floor size, and market trends. Traditional valuation techniques often rely on domain experts, which may be time-consuming and less adaptable to market changes. Machine learning offers a powerful alternative by learning patterns from historical data to make reliable predictions. By integrating these capabilities into a web system, users gain access to instant valuation tools from any location.
Problem Statement
The Tanzanian housing market, like many others, lacks accessible digital tools to accurately estimate house prices. This gap makes it difficult for homebuyers and sellers to evaluate properties objectively. Moreover, the absence of locally-tuned prediction models means that many tools, if available, are trained on foreign data, making them less accurate in the Tanzanian context. This project aims to solve that problem using locally relevant data and ML models.
2. Objectives
General Objective:
To develop a machine learning-based web application capable of predicting house prices in Tanzania using structural and geographic features.
Specific Objectives:
- Design a secure and user-friendly web platform using Django.
- Collect and preprocess housing data for model training.
- Train and compare multiple machine learning algorithms (e.g., Linear Regression, Random Forest).
- Integrate the trained model into the Django application for real-time prediction.
- Implement features such as user registration, login, and password reset for security.
3. System Overview
Main Features:
- User Authentication: Login and signup features secured with Django's authentication system.
- House Price Prediction: Users input features like square footage, rooms, and neighborhood.
- Currency Conversion: Predicted prices in USD are converted to Tanzanian Shillings (TSH).
- Admin Panel: Django's built-in admin site allows superusers to manage data and users.
- Password Reset Flow: Users can recover their account credentials using a secure email-based reset process.
4. Technologies Used
Category	Tools/Frameworks
Language	Python 3.x
Web Framework	Django 5.2
Frontend	HTML, CSS (with glassmorphism UI design)
ML Libraries	scikit-learn, pandas, numpy
Database	SQLite (default Django DB for prototyping)
Environment	Localhost / Development Server
5. System Architecture
Frontend:
HTML and CSS templates are used to create an interactive and responsive user interface. Pages include the login screen, signup form, house price prediction form, and password reset interfaces. The interface uses modern CSS techniques such as flexbox layout and glassmorphism styling for aesthetic and usability benefits.
Backend (views.py):
The backend is powered by Django views, which handle user authentication, form processing, price prediction, and password reset logic. These views ensure that each request is securely handled and properly validated before interacting with the model.
Model Integration:
A custom utility (`utils.py`) processes the input from forms and uses trained ML models to predict prices. The dataset (`housing_price_dataset.csv`) is preloaded into memory at runtime for performance.
6. Password Reset Feature
Password reset is implemented using Django’s built-in authentication views, which follow a secure multi-step process. Users can request a reset link via email, confirm their identity through a tokenized link, and set a new password. The email backend is configured to display messages in the console for development. Templates are fully styled to match the rest of the application.
URL Paths Include:
- `/password_reset/`: Email form for requesting a reset.
- `/password_reset_done/`: Confirmation screen.
- `/reset/<uidb64>/<token>/`: Secure reset link.
- `/reset/done/`: Final confirmation.
7. Evaluation
Model performance was evaluated using standard regression metrics. A subset of the original dataset was used to test the models, ensuring real-world applicability and avoiding overfitting.
Metric	Value (Example)
RMSE	52,304.31
MAE	42,110.21
R²	0.87
8. Conclusion & Recommendations
This project demonstrates how machine learning can be integrated into practical web applications to solve local real-world problems. The system is flexible and scalable, allowing for future enhancements such as real-time data integration, geolocation-based predictions, and user profile history.
Recommendations:
- Use a production-ready database like PostgreSQL for deployment.
- Add charts or visual insights on the prediction result page.
- Implement an admin dashboard for dataset management.
- Enable export of predictions for offline use (e.g., PDF reports).
9. References
1. Antipov, E., & Pokryshevskaya, E. (2012). Mass appraisal of residential apartments using ML.
2. Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system.
3. Tanzania National Bureau of Statistics (2022). Census Report.
4. Django Documentation (2024). https://docs.djangoproject.com/
5. Scikit-learn Documentation. https://scikit-learn.org/

![WhatsApp Image 2025-06-05 at 15 55 20_1c335704](https://github.com/user-attachments/assets/fb4238ca-3d16-45b1-973f-bc1acef0b25d)





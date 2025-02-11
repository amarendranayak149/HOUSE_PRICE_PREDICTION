# House Price Prediction App

## Overview
This is a Streamlit-based web application for predicting house prices based on user inputs. The model used in this app is a trained Linear Regression model stored in a pickle file.

## Features
- Interactive UI using Streamlit
- User inputs for square footage, number of bedrooms, number of bathrooms, neighborhood type, and year built
- Prediction of estimated house price

## Installation
1. Clone this repository or download the source files.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

## Dependencies
Make sure you have the following libraries installed:
- `streamlit`
- `numpy`
- `pandas`
- `scikit-learn`
- `pickle`

## Usage
1. Run the application.
2. Enter the required details:
   - Square Feet
   - Number of Bedrooms
   - Number of Bathrooms
   - Neighborhood type (Rural, Semi-Urban, Urban)
   - Year Built
3. Click the **Predict Price** button to get the estimated house price.

## Model Information
- The model is a **Linear Regression model** trained on a housing dataset.
- The model file (`elite27.pkl`) is loaded in `app.py` to make predictions based on user inputs.

## File Structure
```
|-- app.py                   # Streamlit app
|-- elite27.pkl              # Trained model
|-- House Price Prediction.ipynb  # Jupyter Notebook for model training
|-- README.md                # Project documentation
```

## Acknowledgments
This project was created by **Amarendra Nayak** as part of a Data Science initiative.

## Contact
For any queries or collaborations, feel free to reach out!

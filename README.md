# Eyes-Color-Prediction

A machine learning project for predicting eye color using a trained model with a web-based interface.

## Project Structure

- `1.csv` - Dataset containing eye color data
- `app.py` - Flask web application
- `train.ipynb` - Jupyter notebook for model training and experimentation
- `templates/index.html` - HTML template for the web interface
- `README.md` - Project documentation

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Jupyter Notebook (optional, for model training)

## Installation

1. Clone or download this repository:
   ```bash
   cd Eyes-Color-Prediction
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training the Model

To train or experiment with the model:

1. Open Jupyter Notebook:
   ```bash
   jupyter notebook train.ipynb
   ```

2. Run the cells in sequence to:
   - Load the dataset from `1.csv`
   - Preprocess the data
   - Train the model
   - Evaluate model performance

## Running the Application

1. Start the Flask web application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Use the web interface to make eye color predictions

## Usage

1. Access the web interface at `http://localhost:5000`
2. Input the required features
3. Click predict to get the eye color prediction
4. View the results on the page

## Features

- Machine learning model for eye color classification
- Web-based user interface
- Real-time predictions
- Simple and intuitive design

## Notes

- Ensure the dataset (`1.csv`) is in the project root directory
- The model should be trained before running predictions
- Make sure all dependencies are installed before running the application
# Linear Regression

A simple implementation of linear regression to predict car prices based on mileage.

## Project Structure

- `src/train_model.py`: Trains the linear regression model using gradient descent
- `src/estimate_price.py`: Estimates car prices using the trained model
- `src/evaluate_model.py`: Evaluates model performance with metrics like MSE, RMSE, MAE, and R²
- `data/data.csv`: Dataset containing car mileage and price information
- `output/`: Directory where model parameters and plots are saved

## Usage

1. **Train the model**:
   ```bash
   python src/train_model.py
   ```

2. **Estimate a car's price**:
   ```bash
   python src/estimate_price.py
   ```

3. **Evaluate model performance**:
   ```bash
   python src/evaluate_model.py output/model.npy
   ```

## Dataset

The dataset (`data/data.csv`) contains car mileage and corresponding prices:
- 24 entries of car mileage (km) and price ($)
- Used to train and evaluate the linear regression model

## Resources

- [Linear Regression Explained](https://www.youtube.com/watch?v=Jj7WD71qQWE)
- [Partial Derivatives](https://www.youtube.com/watch?v=AXH9Xm6Rbfc)


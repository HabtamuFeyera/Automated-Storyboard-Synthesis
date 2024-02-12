from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from model_development.model_architecture import StoryboardModel

def hyperparameter_search(train_data, validation_data):
    # Define hyperparameters to tune and their search spaces
    param_grid = {
        'learning_rate': [0.001, 0.01, 0.1],
        'batch_size': [32, 64, 128],
        # Add other hyperparameters and search spaces here
    }

    # Perform hyperparameter search using grid search or randomized search
    # grid_search = GridSearchCV(StoryboardModel(), param_grid, cv=3)
    randomized_search = RandomizedSearchCV(StoryboardModel(), param_grid, cv=3)
    randomized_search.fit(train_data, validation_data=validation_data)
    return randomized_search.best_params_

if __name__ == "__main__":
    # Load preprocessed data
    train_data, validation_data = load_data()

    # Perform hyperparameter tuning
    best_params = hyperparameter_search(train_data, validation_data)
    print("Best hyperparameters:", best_params)

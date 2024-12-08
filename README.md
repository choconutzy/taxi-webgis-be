# Backend

## Setup
### Environment Variables
Please create .env file in the taxi directory. Please refer to the settings.py file for the environment variables that need to be set. The following is an example of the .env file:
```
DB_HOST=<db_host>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_NAME=<db_name>
```

### Initialize the Project
Run these commands to initialize the project:
```

# Setup the virtual environment
python -m venv webgis_venv

# Activate the virtual environment
source webgis_venv/Scripts/activate

# Install the dependencies
pip install -r requirements.txt

# Run the migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

## Running the Tests

Run these commands to run the tests:
```
# Create new virtual environment
python -m venv webgis_venv 

# Activate the virtual environment
source webgis_venv/Scripts/activate

# Install the dependencies
pip install -r requirements.txt
conda install -c conda-forge gdal

# Run the tests
python manage.py test
```

Although when in the environment, you can run the tests with the following command:
```
python manage.py test
```

## Running the Server

Run these commands to run the server:
```
# Create new virtual environment
python -m venv webgis_venv 

# Activate the virtual environment
source webgis_venv/Scripts/activate

# Install the dependencies
pip install -r requirements.txt

# Run the migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

## In staging and production
Run these commands to update the server:
```
# Create new virtual environment
python -m venv webgis_venv 

# Activate the virtual environment
source webgis_venv/Scripts/activate

# Install the dependencies
pip install -r requirements.txt

# Run the migrations
python manage.py migrate

# Run the server
sudo systemctl restart gunicorn
```
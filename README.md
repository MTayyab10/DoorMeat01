# DoorMeat01
    A simple booking service app

### How to run a Clone (from GitHub) Django Project?

First, need to install all requirements of project by running following command.

`pip install -r requirements.txt`

1. Install virtualenv with pip:

    ``` pip install virtualenv ```
2. Create new virtual env with python3:

    ```virtualenv venv -p full_path_to_python` # e.g. use `where python` to find the path to correct python    
3. Activate virtual env:

```venv\Scripts\activate```

4. Install dependencies:
pip install -r requirements.txt

After that you have to configure the database.You have to make migrations and then migrate.

`python manage.py makemigrations `

to create migration files for the models already defined in the codes you have cloned.

`python manage.py migrate`

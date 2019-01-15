# STEP 1: create the project

## How to get here

1. Create the skeleton

```bash
cookiecutter gh:candidtim/cookiecutter-flask-minimal
```

Input project name and package name respectively when asked:

* project name: `meal-options`
* package name: `meal_options`


2. Install dependencies

```bash
cd meal_options
pipenv --python 3
pipenv install flask
```

3. Update settings and app creation:

edit following files, content can be copied from the repo:

* `meal_options/meal_options/settings.py`
* `meal_options/meal_options/app_factory.py`
* `meal_options/meal_options/__init__.py`

4. Test:

```bash
pipenv shell
FLASK_APP=meal_options flask run
```


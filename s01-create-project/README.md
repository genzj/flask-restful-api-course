# STEP 1: create the project

1. Create the skeleton

```bash
cookiecutter gh:candidtim/cookiecutter-flask-minimal
```

When being asked, input following project name and package name:

* project name: `meal-options`
* package name: `meal_options`

1. Install dependencies

```bash
cd meal_options
pipenv --python 3
pipenv install flask
```

1. Update source code:

delete following unnecessary placeholder folders and files:

* `meal_options/Makefile`
* `meal_options/meal_options/static/`
* `meal_options/meal_options/templates/`
* `meal_options/meal_options/views.py`

edit following files (check corresponding file in this repo for details):

* `meal_options/meal_options/default_settings.py`
* `meal_options/meal_options/__init__.py`

add a new file for our business logic:

* `meal_options/meal_options/app.py`

1. Test:

   ```bash
   pipenv run flask --app meal_options.app run
   ```

   Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.
   You're supposed to see `Hello World` in the browser.

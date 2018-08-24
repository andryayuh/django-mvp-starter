# todolist
simple django app todolist

## Setup

**Requirements**:

 - Postgres
 - Python 3
 - Pipenv (`pip install pipenv`)

 **Steps**

  - `pipenv install` or `pipenv install --dev`

    *This will install all python dependencies from the Pipfile. Adding `--dev` will also install dev dependencies.*

**To enter on your environment**

`pipenv shell`

**To run locally**

`python3 manage.py runserver`
`python3 manage.py migrate`

**To add a new package**

`pipenv install package_name`

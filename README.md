# DataProject django rest framework

## Technilogies

1. Front-end :- HTML, Bootstrap 4

2. DataBase :- PostgreSQL

3. Backend :- Django, Django-Rest_Framework

## How to run

After Cloning the project Move in side the Outer **drf** directory which will contain __drf__ directory and some file.
Perform steps 1 to 4 in this directory. For steps 5 to 8 cd into inner **drf** directory.

### Run following command step by step in Treminal

   1. Create python virtual environment and activate it.

      ```console
      $ python3 -m virtualenv env
      $ source env/bin/activate
      ```

   2. Install requirements from requirements.txt

      ```console
      $ pip install -r requirements.txt
      ```

   3. Download .csv file in the same directory where virtual environment is created

      ```console
      $ curl -O https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv
      ```

   4. Run create.sql script to create User and databse

      ```console
      $ psql < create.sql
      ```

   5. Change directory

      ```console
      $ cd drf/
      ```

   6. Run Migrate command

      ```console
      $ python manage.py migrate
      ```

   7. Populate DB with data from population-estimates.csv data.

      ```console
      $ python manage.py data_loader **.csv file name**
      ```

   8. Run the Server.

      ```console
      $ python manage.py runserver
      ```

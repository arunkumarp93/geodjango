# Mozio Providers API

Checkout the [Documentation](https://moziosampleapp.docs.apiary.io/)

## Local Dev setup

1.  Pull the code from repo

2. create new virtualenvironment and activate it. Then install the requirements
  
`pip install -r requirements.txt`

3. run makemigrationa and migrate

`python manage.py makemigrations`

`python manage.py migrate`

4. create superuser

`python manage.py createsuperuser`

5. Run the server

`python manage.py runserver`

Now we can get the list of providers and location in [API Root URL](http://localhost:8000/v1).

Add new providers through  admin and API

## Assumptions and limitations

1. Mobile number is international (gave 16 digit length) with or without country code is allowed.

2. Language is added as code with max length of 3 [ISO-639](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

3. GeoJSON field is used as MultiPolygonField.

4. Currency are assumed as international and used [ISO-4217](# https://en.wikipedia.org/wiki/ISO_4217).

5. leaving the security key and sqllite3 for the localdev testing purpose.

6. Local machine must have [spatialite](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/spatialite/) and GDAL available.
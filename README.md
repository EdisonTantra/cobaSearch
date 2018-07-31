# CobaSearch

Diseases search based on symptoms in Bahasa with elasticsearch and django.

# Before you go
## Clone this repo
>git clone https://github.com/EdisonTantra/cobaSearch.git

## Install Elasticsearch and run it
###### **(Work on Elasticsearch 6.2.4)**

> [Download and Install Elasticsearch](http://https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html "Download and Install Elasticsearch")

>bin/elasticsearch

## Make your virtualenv
###### if you don't have virtualenv
>[Install virtualenv](https://virtualenv.pypa.io/en/stable/installation/ "Install virtualenv")

###### run virtualenv
>virtualenv elasticsearchEnv

>source elasticsearchEnv/bin/active

## Install dependencies
>pip install -r requirements.txt

## Make migrations for django
>python manage.py makemigrations

>python manage.py migrate

## Run Django in localhost (Default Port : 8000)
>python manage.py runserver

# Test it!

## Check everthing is good :
 **Method**|  GET  
 --------- | ---------
  **URL**  |  *localhost:8000/api/*

## Setup:
 **Method**|  GET  
 --------- | ---------
  **URL**  |  *localhost:8000/api/setup*

## Search:
 **Method**  | POST  
 ----------- | -----------
  **URL**    |  *localhost:8000/api/search* 
 **Header**  | Content-Type : application/json,  X-CSRFToken : csrfToken
  **Data**   | symptom1, symptom2, symptom3

**Thanks!**
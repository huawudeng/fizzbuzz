# Introduction

This package uses the pretrained model "distilbert-base-uncased-finetuned-sst-2-english" from HuggingFace text classification models for sentimental analysis. Compared with BERT, the distilbert is smaller and faster with insignificant loss of accuracy.

Django was used to create the code structure of this package. The entire package can be deployed into a Docker container.

# Functionality

The key function for sentimental analysis is implemented in the code hgface/sentiment/sentiment/views.py, where the pretrained model is loaded and applied to incoming text request.

The testing code is implemented in the code hgface/sentiment/test.py, in which a fixed number of requests are posted to the app and the returned analyzed results are printed out.

# Testing without Docker

This package can be tested without using Docker. Following are the steps:

>cd hgface/sentiment

>python manage.py runserver

>python tests.py

You will see 100 lines printed out in the screen. Each line tells the sentiment of the text and the confidence score.

# Build Docker Image

The two key configuration files for building Docker image are hgface/Dockerfile and hgface/docker-compose.yml. 

Run the following command in a powershell to build a Docker image and bring it up running as a container:

> cd hgface
> docker-compose up --build

Two images/containers will be built and up running, one as NGINX server (reverse proxy server) and another one as web application.

However, in my own laptop (Windows) environment, I could not test the inferencing successfully although both NGINX and web application (sentiment on Gunicorn) are up running successfully. The reason could be incorrect configuration of the proxy_pass for NGINX or firewall settings in the OS level.

I did not have more time for further troubleshooting and computer networking is indeed NOT my strength.



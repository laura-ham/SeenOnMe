# SeenOnMe

This project is a submission for Junction 2019 in reference to the challenge posed by Columbia Road. The aim of this project is to provide a novel method to reduce the return ratio in e-commerce platforms. We do this by providing an added tool for the customers to have a feel and look of the product by having access to experiences of the community. 

The project consists of a Google App Engine based API and database as the core engine, along with a sample [Angular JS application](https://github.com/irisfffff/seenonme-junction2019).

## Setup

In order to setup the core engine, you need the following components

- Google Cloud SDK
- Python 2.7
- Pip

In order to install the third party components run the following code.
```
mkdir lib
pip install -r requirements.txt -t libs/
``` 

In order to deploy, the following code can be used, given a Google App Engine project is created first.
```
gcloud app deploy
```

The Angular project can run either locally or on a web service, via NodeJs SDK. Remember to modify the server link.
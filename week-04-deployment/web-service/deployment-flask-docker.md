# Deployment

In this section, we will see how we can deploy a machine learning model into production as a web service.

>Note : I'll be doing this locally as I don't have AWS account because my Rupay card is not being accepted :(

# Let's start 🚀

![lets begin](https://media0.giphy.com/media/5zf2M4HgjjWszLd4a5/giphy.gif)

## What exactly do we need ? 

For deploying model in Online mode, we had seen that we can do it using a web service.  
We also saw a general flow of how this system works as follows : 

![flow](https://user-images.githubusercontent.com/55437218/178157777-ed24f4b0-e05a-48f5-ba37-cc3642f2ba31.png)

So what components do we need ?

1. Something which sends a Http/Https request, e.g. backend
2. Machine Learning model
3. Something which handles that request and passes that information to our model and returns the result, e.g. Flask API  

So lets build everything up !

## Setup

Before diving into the implementation, lets take a deep breathe and setup a virtual environment
> A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python environment

We will be using the package [pipenv](https://pypi.org/project/pipenv/)
> I used to use virtualenv before but this does eliminates lot of steps required in virtualenv

### Installation :

```bash
$ pip install --user pipenv
```

For this tutorial, we will need only two packages, i.e. scikit-learn and flask 

```bash
$ pipenv install scikit-learn==1.0.2 flask
```

> Note : 1.0.2 version of scikit-learn is obtained by doing `pip list | grep scikit-learn` in the environment where model was trained
> We can also pass a requirements.txt while doing pipenv install to install those packages in requirements

This basically creates `Pipefile.lock` file which stores all the information about installed packages (tracks it automatically)

![pipenv output](https://user-images.githubusercontent.com/55437218/178158790-a15fb012-53df-4e65-8cc5-35f87ae19816.png)

Activate the virtual environment with

```bash
$ pipenv shell
```
This activates the virtual environment 
![activate virtualenv](https://user-images.githubusercontent.com/55437218/178158937-e31e3391-265a-4de9-988a-0dff181839e8.png)

As you can see prompt looks tooo long, so we can change it by changing the environment variable `PS1`
![PS1 changed](https://user-images.githubusercontent.com/55437218/178158961-f5a7f39b-dea2-4df9-857f-21ad0c990c5a.png)

### Machine Learning model 

We will be using [linear regression model](../week-02-experiment-tracking/mlruns/1/072cc28abdcc40f3bede9f43c0518122/artifacts/models_pickle/lin_reg.bin), 
which we had trained last time in week-02 of experiment tracking

### Flask API 

Flask is a web application framework in python which can be used to create APIs. 

First we will create some utility functions to help us load our model and prepare the data coming from the http request

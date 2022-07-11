# Deployment : Web service 👔

In this section, we will see how we can deploy a machine learning model into production as a web service.

>Note : I'll be doing this locally as I don't have an AWS account because my Rupay card is not accepted :(

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
> We can also pass a `requirements.txt` while doing pipenv install to install those packages in requirements

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

```python
import pickle

# loading model with dict vectorizer
def load_model(path='lin_reg.bin'):
    with open(path, 'rb') as f_in:
        (dv, model) = pickle.load(f_in)
        return (dv, model)

# from ride(dictionary) we take only the features which we used to train our model
def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

# function to predict prepared features
def predict(features, dv, model):
    X = dv.transform(features)
    preds = model.predict(X)
    return float(preds[0])
```

This code can be found in the file : [`utils.py`](utils.py)

Now to crate our api, we will create a file nameed `app.py`

```python
from flask import Flask, request, jsonify
from utils import *

# define our app
app = Flask("nyc-taxi-duration")

# load model and vectorizer
dv, model = load_model("lin_reg.bin")

# /predict-duration endpoint to talk with our API
@app.route("/predict-duration", methods=["GET"])
def predict_duration():
    """Returns JSON response of predicted duration for the data obtained from the body of incoming request"""
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features, dv, model)

    result = {"duration": pred}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
```

So what this is does is, whenever we send a `GET` request to our API at the endpoint `/predict-duration` it performs the function `predict_duration()`  
Inside the function, it grabs the `json` data we sent via http `request` and using the utility functions we made earlier it generates a JSONfied `response`.  
`app.run` runs our server on `localhost` at port `9696`

This code can be found in the file : [`app.py`](app.py)


### Backend

Well we don't have a full fledged app to have a backend that can send https request to our API but what we can do is create a script in python which sends the request!

Create a file `test.py` and paste the following script into it

```python
import requests

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

url = 'http://localhost:9696/predict'
response = requests.get(url, json=ride)
print(response.json())
``` 

Script is pretty straight-forward...

>Note: run this script outside your virtual environment as we haven't installed requests library in our environment

### Lets test the server

Run the server using,
`$ python app.py`
![image](https://user-images.githubusercontent.com/55437218/178159988-71ca2944-4b35-44ae-9084-237e60c57111.png)

Now let's try our test script to see if our API actually works or not

![response output](https://user-images.githubusercontent.com/55437218/178160159-e174f798-8087-443b-97f0-45ec5715e963.png)

BOOM 🎆

![BOOM](https://media1.giphy.com/media/l3q2zxUCPX4rmO8ZG/200w.gif)

### Gunicorn server

If you look closely, when we start our Flask API it says:
![flask warning](https://user-images.githubusercontent.com/55437218/178160360-86b6eb47-fc5c-40d2-8d29-b6dced523e60.png)

oof so what to do in production then?
WE USE gunicorn server !

It is a Python WSGI Server for UNIX

So install it with
```bash
$ pipenv install gunicorn
```

>Note: If you check Pipfile, then you'll see that it has been automatically updated with the new package which is quite useful :)

Remove `if __main__` part from our `app.py`
and run the gunicorn server by simply doing : 

```bash
gunicorn --bind=0.0.0.0:9696 app:app
```
This basically says gunicorn server to setup a server at address `0.0.0.0` and port `9696` and in the file `app` look for `app` (Flask app)

Thus we've a gunicorn server running :
![gunicorn server](https://user-images.githubusercontent.com/55437218/178160516-d5a3598f-d120-432c-acb0-23ff9a9c6676.png)

## THE END ? NO XD

So we've successfully created 
* Created a virtual environment with pipenv
* Created a Flask API 
* Tested API with http request
* Used gunicorn to run our API in production mode

There's a one problem tho... 🤔

What if your production environment or the machine on which you're hosting this API does not support the version dependencies which we have ?
What if production environment has a different configurations that the one which have in local?
What if you developed this application on windows 10 but some packages are not supported in Ubuntu which is used in production environment 👀

Well that's why we've  

![docker meme](https://media.makeameme.org/created/docker-i-see.jpg)


> Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. Using Docker, you can quickly deploy and scale applications into any environment and know your code will run.
[Source](https://aws.amazon.com/docker/)

# Dockerizing API 

In next step, we will wrap our web API inside docker container which will act as a isolated environment for our API to run.

![docker api diagram](https://user-images.githubusercontent.com/55437218/178342671-c3836c44-c0cd-4a09-890d-bd76b2aa6ab2.png)

Make sure docker service is available at your system. You can checkout my guide on [Setup](https://github.com/pathikg/MLOps-Zoomcamp-DataTalks/blob/main/week-01-introduction/Setup.md) for Windows machine.

So lets building Docker `image` with `Dockerfile` 

>A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

Create a filed named `Dockerfile` to write following instructions which we'll be using to create our docker image

1. Select image to be used 

```Docker
FROM python:3.9-slim
```

Here we're telling our docker to build a `Python` image having a tag `3.9-slim`

>I think `3.9-slim` is a lightweight image   
> (I am a noob so pls correct me if I am wrong)

You can find more about python docker images at [dockerhub](https://hub.docker.com/_/python)

2. Installing Pipenv

We need to make sure that `pip` and `pipenv` is installed in our image so that we can install packages inside our `Pipefile` 

```Docker
RUN pip install -U pip
RUN pip install pipenv 
```
3. Specifying a working directory

```Docker
WORKDIR /app
```

4. Copying Pipefile from local directory to docker image

```Docker
COPY [ "Pipfile", "Pipfile.lock", "./" ]
```

5. Installing packages using pipenv

```Docker
RUN pipenv install --system --deploy
```

6. Copying model and API into our docker image

```Docker
COPY [ "app.py", "utils.py", "lin_reg.bin", "./" ]
```

7. Openup the port

Since we are using port `9696` to communicate with our API

```Docker
EXPOSE 9696
```

8. Startup Server

Whenever our docker container is initiated, we want to start the server hence

```Docker
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "app:app" ]
```

9. Build our docker image 

As we are done with the instructions, its time to build our docker image from the instructions which we just specified

In terminal,
```bash
docker build -t ride-duration-prediction-service:v1 .
```

You'll see something like this :
![docker build output](https://user-images.githubusercontent.com/55437218/178354440-dd77607d-2553-45ec-a93f-2afaec4f103b.png)


You can confirm your build by doing :
```bash
docker images
```
![docker images output](https://user-images.githubusercontent.com/55437218/178354034-4ef2feef-3252-464d-8787-6c589e7ebe73.png)


So let's test it out ?

```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```

i.e. `docker` sir pls run our docker container named `ride-duration-prediction-service` with version `v1` in interactive mode `it` and delete it afterwards `rm` and yes pls map port `9696` in docker container to `9696` on Docker host

![docker server running](https://user-images.githubusercontent.com/55437218/178354381-6eca3222-e59d-4c87-b1dd-0844048154a5.png)

test it using `test.py`  

There we go...  
![image](https://user-images.githubusercontent.com/55437218/178354709-2592e3f7-6f4b-4863-9389-3ada46a339e0.png)

Thus we've successfully dockerised our Flask API 

![yes dance](https://thumbs.gfycat.com/BlackFineChicken-max-1mb.gif)

See ya later...  
BYE BYE 🤙

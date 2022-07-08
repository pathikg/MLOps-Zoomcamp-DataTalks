# Deployment 🚀

Well till now, we've
* Designed our model 
* Done some experiments with our model (with MLFlow and model registry)
* Created workflow pipelines (using prefect)

So what's next ❔  

![what](https://media4.giphy.com/media/ghuvaCOI6GOoTX0RmH/giphy.gif)

well everything we've done till now is fine but whatever model we've created is not yet used for its respective purpose right ?
I mean its just sitting somewhere in the dark forest of our code ... :(

IN SHORT,
Now its time to do something so that we can use whatever model which we've created into an actual use ...  

![lets start](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiuoxTcVCqzCqUvb6ujYQtwvnODJXQWxaqEg&usqp=CAU)


# What does it mean to deploy a model 🤔?

Model deployment is a process of exposing our model to its respective production related environment  

e.g.  
Let's say we've created a model which identifies whether or not person has a brain tumour based on his/her brain MRI scans.   
To use this model in real life we need to integrate that model with an application cuz doctors are not going to open up their VS Code 
and clone our GitHub Repository and then pass that image to get the predictions right ? XD  
i.e. We have to provide a way for a regular person to use our model which can be obtained by storing our model in the cloud and loading it in the backend then 
maybe taking MRI scans from the users as a input on the website and passing it into our model thereby showing the predictions back on the frontend

# Modes of model deployment

* Batch/Offline mode : when we require model to do tasks at regular intervals
* Online : when we require model to be running all the time
  * Web service : model can be available as an API where we can send an http request and get the predictions back in the response e.g. image prediction  
  * Streaming : when there is a stream of events and model service is listening to those events to react respectively e.g. realtime object detection task
  
 

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

![lets start](https://y.yarn.co/9b3d38e4-30a7-4907-b156-d8310815ff92_text.gif)


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
  * Web service : model can be available as an API where we can send an http request and get the predictions back in the response
  * Streaming : when there is a stream of events and model service is listening to those events to react respectively
  

## Batch or Offline mode : 
 
In this mode, we only need our model to be used on regular intervals of time (e.g. hourly, monthly, weekly, etc.)
Model is usually train on a batch of data

e.g.  
Company forecasting sales for next month at the end of current month  

Overall flow in this mode kind of goes like this : 

![Batch mode flow](https://user-images.githubusercontent.com/55437218/178050769-28b80652-6fcf-41c3-bc38-cb389494dc68.png)

This technique is used a lot in marketing use cases such as **Customer churn**
> Customer churn, also called customer attrition, is the number of paying customers who fail to become repeat customers. 
[source](https://www.techtarget.com/searchcustomerexperience/definition/customer-churn-customer-attrition)

## Online mode : Web service 

In online mode, we need our model running all the time

e.g.  
Brain tumour detection model, which needs to be running all the time since we can have doctors all around the world using it anytime 

Overall flow in this mode goes like this :  
![web service flow](https://user-images.githubusercontent.com/55437218/178052034-763a42ce-815c-43bd-91a3-ae4254e8fefa.png)


## Online : Streaming

In this model, we have stream of events and model service is listening to those events to react respectively

e.g.
You booked a cab, then before booking (event 1) you got to know "estimated fair" of trip which could be done by one model then as the ride started (event 2) another model triggered which calculates "trip duration", and so on ... 

Flow of this system can be visualized as follows : 
![streaming flow](https://user-images.githubusercontent.com/55437218/178053966-7d0b2fb4-a909-4295-b4a0-bb6321749972.png)

Implementation of such modes will be done in upcoming notes...

Thank you for reading ♥  
![bye bye](https://c.tenor.com/dj5RjDdGALcAAAAM/stanley-the-office.gif)

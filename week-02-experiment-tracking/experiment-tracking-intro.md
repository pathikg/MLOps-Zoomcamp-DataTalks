# 🔍 Experiment Tracking 🔍

## Experiment ❔ What's that ❔

In the context of Machine Learning, ML **Experiment** can be thought as process of building a model  
which includes : 

📖 Source code  (e.g. Tensorflow or PyTorch)  
🌳 Environment  (e.g. CPU or GPU)  
📊 Data  (e.g. Train-Test Split, Selected Features, Data Cleaning Technique, etc. )  
🤖 Model  (e.g. Naive Bayes, XGBoost, NN, etc.)  
📈 Optimizer  (e.g. Adam or SGD )  
⚙️ Hyperparameters  (e.g. Number of hidden layers, Number of tree in RandomForest, etc. )  
...etc.

## Why is it needed ❔

Well let's say you trained a model with a [random_seed](https://docs.python.org/3/library/random.html)=69 and you gave it to your team for the deployment  
but but but   
After deploying something happened ... 👀  
Model's performance was reduced significantly ⁉️  
similar to this [issue](https://github.com/keras-team/keras/issues/4875#issuecomment-304778367)
 
On some inspection it was found that the `random_seed` used while deployment was set as `42` instead of `69` 🤦‍♂️  
[third point](https://medium.com/mlearning-ai/why-loading-a-previously-saved-keras-model-gives-different-results-lessons-learned-aeea1014e0ba)
Library which you used does some "random" initilizations after loading the model which turned out to be a bit different since the `random_state=42` 

This was just an example of `random_seed`, you may never know if similar thing happens with `learning_rate`, `optimizer`, etc. 🤷‍♂️  
e.g. You trained a `XGBoost` model and saved it (without saving info about parameters) 😴  
Later if an another person who doesn't have any idea about the previous parameters tries to train the model on new data then to he has to find all those parameters cuz if had known the previous parameters then could've started right there to converge faster but since he doesn't knew that ...   

![tata](https://c.tenor.com/4xYdJ6ySbfUAAAAd/tata-bye-bye-rahul-gandhi-funny-meme.gif)

Thus to for **Reproducibility** we need experiment tracking ❕

Same goes with the **Organization** and **Optimization**

## How to track experiments then ? 🤔

Well one way is to have a spreadsheet where you go on adding rows which consists of `Model`, `hyperparameters`, `Scores`, etc. and this is how you can have a track of your **ML Experiments**

![but wait](https://i.imgflip.com/4qam0k.jpg)

* What if in a sleep you entered some wrong values ? 
* How will you decide which things to include in the spreadsheet ?
* Is it interepretable for others ? 

 **AHHHH THATS A LOT OF THINGS TO CONSIDER :(**

To solve all such problems we have tools such as [MLflow](https://mlflow.org/), [weights & biases](https://wandb.ai/), [Neptune.ai](https://neptune.ai/), ... etc.  
In this zoomcamp, we will be specifically using [MLflow](https://mlflow.org/)

## MLflow 
Experiment tracking tool which helps us to track and experiment with features such as 
* Parameters 🔎
* Metrics 👨‍🏫
* Metadata 📃
* Artifacts 📁
* Models 🤖

Along with 
* Author 🎓
* Time ⏱️
* Version ✌️

So that's pretty much it about **Experiment tracking** ❕   
If you liked it then do follow me on [@PathikGhugare](https://twitter.com/PathikGhugare) and lemme know if you have any suggestions :)

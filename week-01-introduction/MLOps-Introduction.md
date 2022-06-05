# What is MLOps ? 
<img src="https://cdn.shapechef.com/graphics-and-templates/stick-figures/thinking-preview.jpg" alt="thinking stickman" style="height:400px;" />


**MLOps** Stands for **Machine Learning Operations** and these are the set practices which one should follow for development and deployment of Machine Learning models  

but you might ask 

# What's the need for MLOps?
Lets understand this with an example,  

For the last couple of years there’s an increase in lot of scams around the United States where scammers pretend to be a Tech Support Group from Microsoft, Amazon, NordVPN, etc. and scam elderly people for thousands of dollars.’

<img src="https://memegenerator.net/img/instances/13143192.jpg" width="300" height="300" alt="tech support meme" align="center"/>


Due to which there’s been a lot of complaints coming from the residents. Authorities found that in nearly 20-30% of those cases were not actually scammers but real service providers who were unsuccessful in providing respective service because of some technical difficulties and thus residents thought it was a scam call.  
So, your task is to determine whether a particular case is of a scam or not, which will help authorities to take fast actions against those scammers

Just like any Machine Learning Project, 
First, you collect the data from the **past 3 months** victims and authorities where you obtain attributes such as 
* `Asked_Remote_Acess` 
* `Opened_Bank_Website` 
* `Location_Of_Call`
* `Money_Asked` 
, etc. and you train a Machine Learning model to predict whether or not a case is of scam or not.

You deployed your model somewhere in a secure cloud, and authorities have started using it...

It’s been a month and authorities have found your ML model useful and they even award you for this brilliancy!

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwf7yVxtTpgHZRkpeTyxB6h2NIhNSaCVspSA&usqp=CAU" width="300" height="300" alt="award" align="center"/>


but but but just after weeks something bad happened...  
Authorities noticed that the lot of cases which were flagged as not scam, came out to be actual scams 


<img src="https://media.makeameme.org/created/sus-60gw8n.jpg" width="300" height="300" alt="SUS" align="center"/>


So they investigated those victims and found that well scammers have **changed** their ways and they've started scamming people with different strategies 
i.e. Input data has been **changed**, its no more `Opened_Bank_Website` cuz now its `UPI_PAYMENTS` and the model is not trained on this change in the data.  
This concept is also known as **Model Drift**  
> Model drift refers to the degradation of model performance due to changes in data and relationships between input and output variables. It is relatively common for model drift to impact an organization negatively over time or sometimes suddenly

AHHH which means now you again have to 
* **Collect** and **intergrate** the new data
* **Train** your model on new data
* **Track** training 
* **Experimentation** with your model
* **Validate** your model 
* **Deploy** your model
* **Monitor** your model 
because you never know when scammers will learn new strategies and your model might fail again :(   
And if it fails then OH MY GOSH you have to perform all those steps **AGAIN**   
but you can do it again right XD ?
<img src="https://c.tenor.com/I7qgI3hGcM4AAAAC/crying-happy.gif" width="300" height="300" alt="pain meme" align="center"/>

Well don't worry cause here's where **MLOps** comes into the picture

<a href="https://imgflip.com/i/6ig3wl"><img src="https://i.imgflip.com/6ig3wl.jpg" width="300" height="300" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>

**MLOps** will provide with you an automated way to do all those steps easily! 

It can help us in
* Model Developement (Designing and Training Model on the new data)
* Continous integration and Continous Deployment (Deploying that model without any interruptions)
* Monitoring (Checking if scammers have found a new strategies)
* Validation (Validating the results obtained)

So yeah that's pretty much it :)  

If you liked it then do follow me on [@PathikGhugare](https://twitter.com/PathikGhugare) and lemme know if you have any suggestions :)

**References** :
* https://www.youtube.com/watch?v=s0uaFZSzwfI 
* https://www.youtube.com/watch?v=ZVWg18AXXuE 
* https://www.techtarget.com/whatis/definition/machine-learning-operations-MLOps

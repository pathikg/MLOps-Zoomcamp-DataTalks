
## 📈 MLOps Maturity Model 

(Taken from the [Notes](https://github.com/LoHertel/Road-to-MLOps/blob/main/01-primer/README.md) made by [LoHertel](https://github.com/LoHertel) )

The extent to which MLOps is implemented into a team or organization could be expressed as maturity. A framework for classifying different levels of MLOps maturity is listed below:


| Lvl |              | Overview | Use Case | 
|----:|--------------|----------|----------|  
| 0️⃣  | **No MLOps** | <ul><li>ML process highly manual</li><li>poor cooperation</li><li>lack of standards, success depends on an individual's expertise</li> </ul> | <ul><li>proof of concept (PoC)</li><li>academic project</li></ul> |
| 1️⃣  | **DevOps but no MLOps** | <ul><li>ML training is most often manual </li><li>software engineers might help with the deployment</li><li>automated tests and releases</li> </ul> | <ul><li>bringing PoC to production</li></ul> |
| 2️⃣  | **Automated Training** | <ul><li>ML experiment results are centrally tracked </li><li>training code and models are version controlled</li><li>deployment is handled by software engineers</li> </ul> | <ul><li>maintaining 2-3+ ML models</li></ul> |
| 3️⃣  | **Automated Model Deployment** | <ul><li>releases are managed by an automated CI/CD pipeline</li><li>close cooperation between data and software engineers</li><li>performance of the deployed model is monitored, A/B tests for model selection are used</li></ul> | <ul><li>business-critical ML services</li></ul> |
| 4️⃣  | **Full MLOps Automated Operations** | <ul><li>clearly defined metrics for model monitoring</li><li>automatic retraining triggered when passing a model metric's threshold</li> </ul>  | <ul><li>use only when a favorable trade-off between implementation cost and increase in efficiency is likely</li><li>retraining is needed often and is repetitive (has potential for automation)</li></ul> |


A high maturity level is not always needed because it comes with additional costs. The trade-off between automated model maintenance and the required effort to set up the automation should be considered. An ideal maturity level could be picked based on the use case / SLAs and the number of models deployed.

If you want to read more on maturity, visit [Microsoft's MLOps maturity model](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model).

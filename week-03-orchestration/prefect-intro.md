
# ![image](https://user-images.githubusercontent.com/55437218/177183197-63ce8d4a-2d48-44d9-9641-fa2faa3feac9.png)

[Prefect](https://www.prefect.io/) is a tool that enables us to build, run, and monitor data pipelines at scale.

# Installation 

Installing the latest version

```bash
pip install -U "prefect>=2.0b"
```

# Usage

To demonstrate its usage, I will be using the code from [experiment-tracking](/week-02-experiment-tracking/) module
but first the code in the jupyter notebook needs to be converted into script since we will be using scripts in production environment

Though, Jupyter notebooks can we be used in production but they've their pros and cons 
I found this nice [article](https://neptune.ai/blog/should-you-use-jupyter-notebooks-in-production) which explains a lot on the same

Reformatted script can be found [here](MLOps-Zoomcamp-DataTalks/week-03-orchestration/model_training.py/)

## Let's get started 🥳

### imports

```python
from prefect import flow, task
```

Prefect has two main components flow and task,

### flow 
Flows are the most basic Prefect object. They are containers for workflow logic and allow users to interact with and reason about the state of their workflows  
**In short, it contains the whole logic of our code/workflow**

e.g. In our use case, we can include the whole logic in a single function say `main()`

```python
@flow
def main(train_path: str = "./data/green_tripdata_2021-01.parquet",
         val_path: str = "./data/green_tripdata_2021-02.parquet"):
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("nyc-taxi-experiment")
    X_train = read_dataframe(train_path)
    X_val = read_dataframe(val_path)
    X_train, X_val, y_train, y_val, dv = add_features(X_train, X_val)
    train = xgb.DMatrix(X_train, label=y_train)
    valid = xgb.DMatrix(X_val, label=y_val)
    # train_model_search(train, valid, y_val) for testing lets not use this :)
    train_best_model(train, valid, y_val, dv) 
 ```

and we can simply call our `main()` function when the script runs
Let's see what do we see in the output :

![flow_main_op](./images/flow_main_op.jpg)


### task

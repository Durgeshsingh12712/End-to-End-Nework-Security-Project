# End-to-End-Nework-Security-Project for Phishing Data

# Environment
```bash
conda create -n Project python=3.10 -y
conda activate Project
```


# Flow Of Modular Coding

### Push Data (Mongo db)

## 1. Steps Data Ingestion
1. Logger
2. Exception 
3. constant-> training_pipeline
4. entity->config_entity->
5. Data_ingestion
6. entity->artifact_entity
7. main.py update for Data Ingestion

## 2. Steps Data Validation
1. Constant
2. Entity-> config_entity -> artifact_entity
3. utils
4. schema.yaml
5. Data Validation
6. main.py

## 3. Steps Data Transformation
1. Constant
2. Entity
3. Utils
4. Data Transformation
5. Main.py

## 4. Step Model Trainer
1. Constan
2. Entity
3. Utils>Ml_util>model>estimator and metric>classification
4. Model Trainer
5. Main.py

## 5. Step MLFLOW
1. Update code (Model Trainer)
2. main.py
3. check experiement 
```bash 
mlflow ui
```

## 6. Add Repo to Dagshub and Track Experiments
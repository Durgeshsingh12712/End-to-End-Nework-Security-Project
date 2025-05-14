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

## 7. App.py
1. update 
2. templates
3. run
```bash
uvicorn app:app --reload
http://127.0.0.1:8000/docs
```
## 8. S3 Bucket Arifact and Final model Upload
1. training_pipeline
2. constant
3. config entity
4. cloud -> s3_synchronizer
5. run 

# Push Model to AWS

## 1. Login to AWS console.

## 2. Create IAM user for deployment

#    Create IAM user with AdministratorAccess
#	 with specific access

	1. EC2 access : It is virtual machine

    Create EC2 machine (Ubuntu) & add Security groups 5000 port

	2. ECR: Elastic Container registry to save your docker image in aws


    Run the following command on EC2 machine



# 3.Create ECR repo to store/save docker image
- save the URI: ```381509086193.dkr.ecr.us-east-1.amazonaws.com/networksecurity ```

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```


### 4. If AWS cli config failed

```bash

sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

sudo apt update

sudo apt install unzip

sudo unzip awscliv2.zip

sudo ./aws/install

```

## AWS
```bash
aws configure
```

# 5. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 6. Setup github secrets:
```bash
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION 

AWS_ECR_LOGIN_URI

ECR_REPOSITORY_NAME

```
# S3 Bucket
![My Image](https://github.com/Durgeshsingh12712/Data-All/blob/main/network/1.%20S3%20Bucket.png)

# CICD Deployment
![My Image](https://github.com/Durgeshsingh12712/Data-All/blob/main/network/2.%20CICD%20Successfull%20Deployement.png)

# Model Launch
![My Image](https://github.com/Durgeshsingh12712/Data-All/blob/main/network/3.%20Launch%20Model.png)

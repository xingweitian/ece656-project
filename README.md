# ece656-project

## Student Information

Name | Student ID | Email
--- | --- | ---
Boyun Zhang | TBA | boyun.zhang@uwaterloo.ca
Weitian Xing | 20757406 | weitian.xing@uwaterloo.ca

## Project Information

Using **lahman2016** as the data set of our project, **Mysql** as the database.

## Tutorial

There are two main parts in our project, server and client. To start with this project, please follow the steps below:

#### Preparement

Download our project:

```bash
git clone https://github.com/xingweitian/ece656-project.git
```

Install all the requirements:

```bash
python3 -m pip install -r requirements.txt
```

Edit **db.json** (You can find it in ***project_folder/server/***, make sure you already had **lahman2016** in your Mysql):

```json
{
  "host": "your db host",
  "port": "your db port",
  "user": "user name",
  "password": "user password",
  "db": "lahman2016"
}
```

#### Run

To run server:

```bash
python3 run.py -s 127.0.0.1:8000
```

To run client:

```bash
python3 run.py -c
```

To see help:

```bash
python3 run.py --help
```

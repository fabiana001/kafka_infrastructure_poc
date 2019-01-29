# wallaroo_kafka_example

## Set up the enviroment

First, create the following directories:

```bash
> cd wallaroo_kafka_example
> mkdir python-virtualenv-machida3
> mkdir wallaroo-src
```

Create a new virtualenv enviroment:
```bash
> python3 -m venv ENV
> source ENV/bin/activate
```

## Run the containers

First run kafka et all. containers:
```bash
> cd docker/kafka
> docker-compose up -d
```

Then, run the wallaroo metric ui and wallaroo kafka producer:
```bash
> cd ../wallaroo
> docker-compose up -d
```

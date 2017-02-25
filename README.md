## Requirements

- docker, docker-compose
- python
- a `voters.csv` in this directory

## Getting setup

Start mySQL server:

```
$ docker-compose run --service-ports db
```

Connect to database on Sequel Pro:

- Host: `127.0.0.1`
- Username: `root`
- Password: `password`

Add database:

1. Click "Choose database..."
2. Choose "Add database..."
3. Name it "database"

Import voters:

```
$ pip install -r requirements.txt
$ python import_voters.py
```

You're done. Now you can run queries such as:

```
select count(*) from voters where city = "Provo" and status = "Active" and party = "Republican";
> 23575
```
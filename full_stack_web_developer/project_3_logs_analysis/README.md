# Logs Analysis
### How to run me
This script uses postgresql database so be sure it is installed in your system.
Next:
- download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file and unzip it
- import the data into the database
```sh
$ psql -d news -f newsdata.sql
```
- fill in correct connection details (username, password) on line 5 in the *main.py* script
- execute *main.py* python script
```sh
$ python3 main.py
```

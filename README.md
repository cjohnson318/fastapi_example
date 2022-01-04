# FastAPI Tutorial

The point of this exercise was to try out [FastAPI](https://fastapi.tiangolo.com/), and try out [dataset](https://dataset.readthedocs.io/en/latest/) as a mock database.

## Python Dependency Install and Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Startup

```bash
make up
make test
```

## Kick the Tires

There's some `requests` code in `test.py`, but you can also interact with this using [httpie](https://httpie.io/). Start the server in one terminal using `make up`, then execute the following commands in another terminal.

```bash
http POST http://localhost:8000/author/create name=Bill
http http://localhost:8000/author/list 
http http://localhost:8000/author/1
http DELETE http://localhost:8000/author/1
http http://localhost:8000/author/list
```

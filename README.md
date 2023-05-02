## open API Worker Document

### First Clone the project:
```python
git clone https://github.com/kaiqueBellmont/openAPIWorker.git
```
### install:
### Docker:
#### Build and get up the container:
```python
docker compose up --build
```
#### Get Down the container:
```python
docker compose down -v
```

## About Worker:
The data that already arrives for the worker is validated and tested.
The real working of the worker is just calling the OpenAPI api for improvements.

Just download the Worker container, and the code analysis API works normally.


# Endpoints:
#### Route: "/" (Home)
#### checks the working of the worker.
##### Return:
##### 200: {"state": "working"}

#### Route: "/insight"
#### param: code_list example:
```python
{
    code_list:[
      {
         "apagar2.py":"import datetime\n\ndef ...},
      {
         "hook/formatter.py":"from dataclasses ..."
      }
    ]
}
```
#### Return: List[str]
##### Example:
```python
[
    "\n\n1. In apagar2.py, for improved readability, the line declaring the variable a should be split into two lines, instead of using an escape character.\n2. In hook/formatter.py, the lines with the parameters of the show_in_code_format method should be properly indented, to be more readable and follow common Python conventions."
]
```
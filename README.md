# Flask Tutorial

This is the Flask tutorial that I followed to learn Flask.

Followed Tutorial URL: https://www.youtube.com/watch?v=Z1RJmh_OqeA

## Requirements:
- Python 3.8+

## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory
3. Create virtual environment
```
$ virtualenv env
```

4. Activate environment:
```
$ .\env\Scripts\activate
```

5. Install the dependencies:
```
$ (env) pip install -r requirements.txt
```

6. Start the web server:
```
$ (env) python app.py
```
Note: Change the server port to the one you want
```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

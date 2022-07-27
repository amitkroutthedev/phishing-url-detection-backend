
# phishing-url-detection-backend

A Rest API which which takes url as input from user and display the result if the url is legitmate or phish.

Based on `python3.8` and `Django4.0`.


## Documentation

From [phishing-url-detection-ml](https://github.com/amitkroutthedev/phishing-url-detection-ml), 
the XGBoost Model had the best result. The model is saved in the ```.sav``` file. We integrate the file 
with the Django app. We also added all the 
15 features in 
the feature. For building the API, we used 
REST API. In the API, we used a GET request to 
get the URL from the client and predict the 
URL through the saved model.
For the safety of the API, we use CORS, 
which allows in-browser requests to your 
Django application from other origins. 
The result is sent to the user in JSON format.

We can get following data form the API
- ```"url"```: Name of the website
- 	```"featureExtraction"```: values of 15 feature extractions from the URL
- 	```"predictionMade"```: If the value is ‘1’ then the URL is a Phishing URL and if the value is ‘0’ then the URL is a Legitimate URL.
- 	```"successRate"```:  The percentage of the URL to a be legitimate.
- 	```"phishRate"```: The percentage of the URL to be a phish.

![image](https://user-images.githubusercontent.com/48612930/181173414-f6c961a0-9052-4ff3-b475-0162a065aed2.png)


## Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://phishing-url-detection-backend.herokuapp.com/)


## Main Features
- The phish/legitmate percentage
- All the 15 feature extraction values
## API Reference


#### Get item

```
  GET https://django-temp-app.herokuapp.com/api/?url=${url}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url`      | `string` | **Required**. the url given by client |



## Screenshots

![image](https://user-images.githubusercontent.com/48612930/181173468-eafcefcc-054a-4506-a24d-3cb699cf60fb.png)


## Run Locally

#### Prerequisites:
 - Have the appropriate Python version.

Install virtualenv

```python
pip install virtualenv
```

Clone the project

```bash
  git clone https://github.com/amitkroutthedev/phishing-url-detection-backend.git
```

Go to the project directory

```bash
  cd my-project
```

Assigning virtualenv name

```bash
virtualenv --python C:\Path\To\Python\python.exe {virtualenv_name}
```

Activating Virtual Enviroment

```bash
.\{virtualenv_name}\Scripts\activate
```

Installing packages

```python
pip freeze > requirements.txt
```

Run the project

```python
django-admin startproject myproject
```

Deactivate the virtual environment

```bash 
deactivate
```
## Contributing

Contributions are always welcome!



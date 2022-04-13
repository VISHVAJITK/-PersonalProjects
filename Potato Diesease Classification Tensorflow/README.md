# Potato Disease Classification

Potato is one of the most cultivated and in-demand crops after rice and wheat. Potato farming dominates as an occupation in the agriculture domain in more than 125 countries. However, even these crops are, subjected to infections and diseases, mostly categorized into two grades: (i) Early blight and (ii) Late blight. Moreover, these diseases lead to damage the crop and decreases its production. In this project, we propose a deep learning-based approach to detect the early and late blight diseases in potato by analyzing the visual interpretation of the leaf of several potato crops. The experimental results demonstrate the efficiency of the proposed model even under adverse situations such as variable backgrounds, varying image sizes, spatial differentiation, a high-frequency variation of grades of illumination, and real scene images.  The training accuracy of the proposed model is obtained to be 93.47% and testing accuracy is 90.8%.

## Demo
Link: https://keen-bombolone-180423.netlify.app/

![img](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/potato.png?raw=true)

## Setup for Python:

1. Install Python ([Setup instructions](https://wiki.python.org/moin/BeginnersGuide))

2. Install Python packages

```
pip3 install -r requirements.txt
```


## Setup for ReactJS

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))
2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))
3. Install dependencies

```bash
cd frontend
npm install --from-lock-json
npm audit fix
```


## Setup for React web-app

1. Go to the [React_app](https://github.com/VISHVAJITK/-PersonalProjects/tree/main/Potato%20Diesease%20Classification%20Tensorflow/react_app ) folder.



## Training the Model

1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village).
2. Only keep folders related to Potatoes.
3. Run Jupyter Notebook in Browser.

```bash
jupyter notebook
```

4. Open `training/potato-disease-training.ipynb` in Jupyter Notebook.
5. In cell #2, update the path to dataset.
6. Run all the Cells one by one.
7. Copy the model generated and save it with the version number in the `models` folder.

## Running the API

### Using FastAPI

1. Get inside `api` folder

```bash
cd api
```

2. Run the FastAPI Server using uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8000`

## Running the Frontend

1. Get inside `api` folder

```bash
cd frontend
```

2. Copy the `.env.example` as `.env` and update `REACT_APP_API_URL` to API URL if needed.
3. Run the frontend

```bash
npm run start
```
## Model Dployment
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.
the fastapi backend is deployed on heroku with [heroku](https://id.heroku.com/login) cli (see the documentation for process) and the React frontend is deployed on [Netlify](https://www.netlify.com/).

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width=170>](https://fastapi.tiangolo.com/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://camo.githubusercontent.com/aeb4f612bd9b40d81c62fcbebd6db44a5d4344b8b962be0138817e18c9c06963/68747470733a2f2f7777772e74656e736f72666c6f772e6f72672f696d616765732f74665f6c6f676f5f686f72697a6f6e74616c2e706e67" width=200>](https://www.tensorflow.org/)[<img target="_blank" src="https://raw.githubusercontent.com/icons-pack/react-simple-icons/8dca56e1f10bda668809f2628adb8908e01a5deb/docs/images/svg/react-simple-icons.svg" width=200>](https://reactjs.org/) 

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/VISHVAJITK/-PersonalProjects/issues) here by including your search query and the expected result

## Future Scope

* Deploy as mobile app
* Optimize Fastapi app.py

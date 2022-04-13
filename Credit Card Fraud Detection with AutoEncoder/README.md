# Credit Card Fraud Detection with Autoencoders

The digital world is growing rapidly. We are used to performing many of our daily tasks
online, such as booking cabs, shopping on e-commerce websites, and even recharging our
phones. For the majority of these tasks, we are used to paying with credit cards. However,
it is a known fact that a credit card can be compromised, which could result in a fraudulent
transaction. The Nilson report estimates that for every $100 spent, seven cents are stolen. It
estimates the total credit card fraud market to be around $30 billion.

Detecting whether a transaction is fraudulent or not is a very impactful data science
problem. Every bank that issues credit cards invests in technology to detect fraud and take
the appropriate actions immediately. There are lot of standard supervised learning
techniques such as logistic regression, from random forest to classifying fraud.
## Building a fraud detection model
For this project, you can download credit card dataset from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud), Andrea Dal Pozzolo, Olivier Caelen, Reid A.
Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for
Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining
(CIDM), IEEE, 2015. 

It consists of credit card transaction data from two days, from
European cardholders. The dataset is highly imbalanced and contains approximately
284,000 pieces of transaction data with 492 instances of fraud (0.172% of the total).
There are 31 numerical columns in the dataset. Two of them are time and amount. Time
denotes the amount of time elapsed (in seconds) between each transaction and the first
transaction in the dataset. Amount is the total amount regarding the transaction. For our
model, we will eliminate the time column as it doesn't help with the accuracy of the model.
The rest of the features (V1, V2 ... V28) are obtained from [Principal Component Analysis](https://ocw.mit.edu/courses/mathematics/18-650-statistics-for-applicationsfall-2016/lecture-videos/lecture-19-video/) of original features for confidential
reasons. Class is the target variable, which indicates whether the transaction was
fraudulent or not.


To pre-process the data, there is not much that needs to be done. This is mainly because a
lot of the data is already cleaned up.
Usually, in a classical machine learning model such as logistic regression, we feed the data
points of both negative and positive classes into the algorithm. However, since we are
using auto-encoders, we will model it differently.


Essentially, our training set will consist of only non-fraudulent transaction data. The idea is that whenever we pass a fraudulent transaction through our trained model, it should detect
it as an anomaly. We are framing this problem as anomaly detection rather than
classification.

for the detailed modelling for the problem you can check above [tutorial.ipynb](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Credit%20Card%20Fraud%20Detection%20with%20AutoEncoder/training.ipynb)

## Results
The following diagram illustrates the loss curves that are generated when the
model is trained for 100 epochs:
![plot](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/epochs100.png?raw=true)

Once the training process is complete, break down the reconstruction error in the testing set
by fraudulent and non-fraudulent (normal) transactions. Generate the reconstruction error
by different classes of transactions:

![reconstructioerror](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/recon1.png?raw=true)
![reconstructioerror](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/recon2.png?raw=true)

The reconstruction error threshold for precision and recall are shown in the following
graph:
![graph](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/precisionrecall.png?raw=true)


The confusion matrix that's obtained from the preceding code is shown in the following
diagram:
![confusionmatrix](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/confusion.png?raw=true)

## Conclusion
We can observe that out of 120 fraudulent transactions, 97 of them have been classified
correctly. However, we have also classified 1,082 normal transaction as being fraudulent,
which will have to go through a manual verification process to ensure a good experience
for the end user.


As a note of caution, we should not assume that auto-encoders are helpful in all binary
classification tasks and can achieve better performance than state-of-the-art classification
models. The idea behind this project was to illustrate a different approach of using autoencoders to perform classification tasks.
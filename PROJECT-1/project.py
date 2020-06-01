import numpy as np
import pandas as pd
import feature_extraction
from sklearn.metrics import accuracy_score

def getResult(url):
    dataset=pd.read_csv(r"phishing_dataset.csv")
    dataset.drop(['index'],axis=1,inplace=True)
    x=dataset.iloc[: ,0:30].values
    y=dataset.iloc[: ,30:31].values
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

    
    from sklearn.tree import DecisionTreeClassifier
    classifier=DecisionTreeClassifier(random_state=0)
    classifier.fit(x_train,y_train)
    decisiontree=classifier.predict(x_test)
    #from sklearn.metrics import confusion_matrix
    #cm=confusion_matrix(y_test,decisiontree)
    #import sklearn.metrics as metrics
    #fpr,tpr,threshold=metrics.roc_curve(y_test,decisiontree)
    #roc_auc=metrics.auc(fpr,tpr)
    accuracy=accuracy_score(decisiontree,y_test)
    print(accuracy*100)
    
    x_new = []
    x_input = url
    x_new=feature_extraction.generate_data_set(x_input)
    x_new = np.array(x_new).reshape(1,-1)
    try:
        prediction = classifier.predict(x_new)
        if prediction == -1:
            return "Phishing URL"
        else:
            return "Legitimate URL"
    except:
        return "Phishing URL"
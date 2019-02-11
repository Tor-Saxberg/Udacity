# pandas tutorial

# reading data
import pandas
data = pandas.read_csv("file_name.csv")

# split the input and output into numpy arrays
# Say we have a pandas dataframe called df, 
# like the following, with four columns labeled A, B, C, D
# to extract A:
df['A']
# outputs:
#    0 1
#    1 5
#    2 9
    name: A, dtype: int64
#to extract more cols use [[...]] 
df[['B', 'D']]
#converting to numpy arrays:
import nympy as np
np.array(df)
# now in one line:
X = np.array(data[['x1','x2']])
y = np.array(data['y'])

######################################################
# fitting classifiers
classifier.fit(X,y)
from sklearn.linear_model import some_classifier
classifier = some_classifier()
classifier.fit(X,y)
#any of: 
# LogisticRegression, 
# MLPClassifier (nueral network), 
# DecisionTreeClassifier
# SVC (support vector machines)
classifier = SVC(kernel = 'poly', degree = 2)
# also "gamma" and "C", both floats

######################################################
# testing  models
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

import random
random.seed(42)

data = np.asarray(pd.read_csv('data.csv', header=None))
X = data[:,0:2]
y = data[:,2]
X_train, X_test, y_train, y_test = 
    train_test_split(X, y, 
                    test_size=0.25, # 25% for testing, 75% for training
                    random_state=42) # for random sampling
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

######################################################
# k-maps, Fscores, and learning curves
train_sizes, train_scores, test_scores = 
            learning_curve( estimator, X, y, 
                            cv=None, n_jobs=1, 
                            train_sizes=np.linspace(
                                .1, 1.0,  num_trainings))
# estimator, is the actual classifier we're using for the data,
# train_sizes are the sizes of data chunks used to draw the curve
# train_scores are the training scores for the trained algorithm 
# test_scores are the testing scores for the trained algorithm 
    #score and error are opposites, so flip the curve in you mind

#The training and testing scores come in as a list of 3 values
#for 3-Fold Cross-Validation.
def draw_learning_curves(X, y, estimator, num_trainings):
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X2, y2, cv=None, n_jobs=1, 
        train_sizes=np.linspace(.1, 1.0, num_trainings))


    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.grid()

    plt.title("Learning Curves")
    plt.xlabel("Training examples")
    plt.ylabel("Score")

    plt.plot(train_scores_mean, 'o-', color="g",
             label="Training score")
    plt.plot(test_scores_mean, 'o-', color="y",
             label="Cross-validation score")


    plt.legend(loc="best")

    plt.show()

 
######################################################

from sklearn.model_selection import GridSearchCV
# Here we pick what are the parameters we want to choose from, and form a dictionary. In this dictionary, the keys will be the names of the parameters, and the values will be the lists of possible values for each parameter.
parameters = {
        'kernel':['poly', 'rbf'],'C':[0.1, 1, 10]}
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
scorer = make_scorer(f1_score)

# Create the object.
grid_obj = GridSearchCV(clf, parameters, scoring=scorer)
# Fit the data
grid_fit = grid_obj.fit(X, y)
t_clf = grid_fit.best_estimator_
# Now you can use this estimator best_clf to make the predictions.



######################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_pts(csv_name):
    data = np.asarray(pd.read_csv(csv_name, header=None))
    X = data[:,0:2]
    y = data[:,2]

    plt.scatter(X[np.argwhere(y==0).flatten(),0], 
            X[np.argwhere(y==0).flatten(),1],
            s = 50, color = 'blue', edgecolor = 'k')
    plt.scatter(X[np.argwhere(y==1).flatten(),0], 
            X[np.argwhere(y==1).flatten(),1],
            s = 50, color = 'red', edgecolor = 'k')
    
    plt.xlim(-2.05,2.05)
    plt.ylim(-2.05,2.05)
    plt.grid(False)
    plt.tick_params(
        axis='x',
        which='both',
        bottom='off',
        top='off')

    return X,y

X, y = load_pts('data.csv')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, make_scorer

#Fixing a random seed
import random
random.seed(42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
         X, y, test_size=0.2, random_state=42)
from sklearn.tree import DecisionTreeClassifier

# Define the model (with default hyperparameters)
clf = DecisionTreeClassifier(random_state=42)

# Fit the model
clf.fit(X_train, y_train)

# Make predictions
train_predictions = clf.predict(X_train)
test_predictions = clf.predict(X_test)

def plot_model(X, y, clf):
    plt.scatter(X[np.argwhere(y==0).flatten(),0], 
            X[np.argwhere(y==0).flatten(),1],
            s = 50, color = 'blue', edgecolor = 'k')
    plt.scatter(X[np.argwhere(y==1).flatten(),0], 
            X[np.argwhere(y==1).flatten(),1],
            s = 50, color = 'red', edgecolor = 'k')

    plt.xlim(-2.05,2.05)
    plt.ylim(-2.05,2.05)
    plt.grid(False)
    plt.tick_params(
        axis='x',
        which='both',
        bottom='off',
        top='off')

    r = np.linspace(-2.1,2.1,300)
    s,t = np.meshgrid(r,r)
    s = np.reshape(s,(np.size(s),1))
    t = np.reshape(t,(np.size(t),1))
    h = np.concatenate((s,t),1)

    z = clf.predict(h)

    s = s.reshape((np.size(r),np.size(r)))
    t = t.reshape((np.size(r),np.size(r)))
    z = z.reshape((np.size(r),np.size(r)))

    plt.contourf(s,t,z,colors = ['blue','red'],alpha = 0.2,levels = range(-1,2))
    if len(np.unique(z)) > 1:
        plt.contour(s,t,z,colors = 'k', linewidths = 2)
    plt.show()

plot_model(X, y, clf)
print('The Training F1 Score is', f1_score(train_predictions, y_train))
print('The Testing F1 Score is', f1_score(test_predictions, y_test))
# We suggest to play with grid search parameters 
# max_depth, min_samples_leaf, and min_samples_split

#First define some parameters to perform grid search on. 
   # We suggest to play with max_depth, min_samples_leaf, and min_samples_split.
#Make a scorer for the model using f1_score.
#Perform grid search on the classifier, using the parameters and the scorer.
#Fit the data to the new classifier.
#Plot the model and find the f1_score.

from sklearn.metrics import fbeta_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier


clf = DecisionTreeClassifier(random_state=42)

# TODO: Create the parameters list you wish to tune.
parameters = {'max_depth':[1,2,3,4,5], 
              'min_samples_leaf':[1,2,3,4,5], 
              'min_samples_split':[2,3,4,5]}

# TODO: Make an fbeta_score scoring object.
scorer = make_scorer(fbeta_score, beta=0.5)

# TODO: Perform grid search on the classifier using 'scorer' as the scoring method.
grid_obj = GridSearchCV(estimator = clf, 
                        param_grid=parameters, 
                        scoring=scorer, 
                        #fit_params=None, 
                        #n_jobs=None, 
                        #iid=’warn’, 
                        #refit=True, 
                        #cv=’warn’, 
                        #verbose=0, 
                        #pre_dispatch=‘2*n_jobs’, 
                        #error_score=’raise-deprecating’, 
                        #return_train_score=’warn’
                       )

# TODO: Fit the grid search object to the training data and find the optimal parameters.
grid_fit = grid_obj.fit(X, y)

# TODO: Get the estimator.

best_clf = grid_fit.best_estimator_

# Fit the new model.
best_clf.fit(X_train, y_train)

# Make predictions using the new model.
best_train_predictions = best_clf.predict(X_train)
best_test_predictions = best_clf.predict(X_test)

# Calculate the f1_score of the new model.
print('The training F1 Score is', f1_score(best_train_predictions, y_train))
print('The testing F1 Score is', f1_score(best_test_predictions, y_test))

# Plot the new model.
plot_model(X, y, best_clf)

# Let's also explore what parameters ended up being used in the new model.
best_clf

#--Modules--
import time

#--Model--
from sklearn.ensemble import RandomForestClassifier

#--Tools--
from preprocessing_titanic import preprocess_data
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


X, y = preprocess_data('Desktop/Python/titanic/data/', 'train.csv', rescale=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

tree = RandomForestClassifier(n_estimators=100, max_depth=10)
tree.fit(X_train, y_train)

start_time = time.time()
print(f"""
Random Forest Model Score: 
Training set: {tree.score(X_train, y_train):.4f} 
Test set: {tree.score(X_test, y_test):.4f}
Cross validation: {cross_val_score(tree, X, y, cv=5).mean():.4f}
Execution Time: {time.time()-start_time:.2f}s\n""")
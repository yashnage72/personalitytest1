import pickle
from sklearn.metrics import accuracy_score
filename = "PP_reg.sav"
loaded_model = pickle.load(open(filename, 'rb'))
a=['0','20','7','9','9','5','5']

print(type(a))

arr=[]
arr.append(0)
arr.append(20)
arr.append(7)
arr.append(9)
arr.append(9)
arr.append(5)
arr.append(5)
print([arr])
Prediction = loaded_model.predict([a])
#print(a.shape)

print(Prediction)



#y_pred_check = loaded_model.predict(arr)
#print(y_pred_check)
#print(accuracy_score(test_y, y_pred_check))
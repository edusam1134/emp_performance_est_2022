import keras
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
import random,hashlib
from sklearn.preprocessing import LabelEncoder
data=pd.read_excel('Data.xlsx')
lab=LabelEncoder()
data['position'] = lab.fit_transform(data['Job role'])
data['department'] = lab.fit_transform(data['Department '])
data['Performance Rating'] = data['Performance Rating'].fillna(data['Performance Rating'].mean())
data['Percent Salary Hike'] = data['Percent Salary Hike'].fillna(data['Percent Salary Hike'].mean())
data['Effected with corona'] = data['Effected with corona'].fillna(data['Effected with corona'].mean())
data['Attendance'] = data['Attendance'].fillna(data['Attendance'].mean())
data['OverTime'] = data['OverTime'].fillna(data['OverTime'].mean())
data['Feedbacks '] = data['Feedbacks '].fillna(data['Feedbacks '].median())
data['Psycho-Social Indicators'] = data['Psycho-Social Indicators'].fillna(data['Psycho-Social Indicators'].mean())
data['Working from home or office '] = data['Working from home or office '].fillna(data['Working from home or office '].mean())
data['Workign hrs '] = data['Workign hrs '].fillna(data['Workign hrs '].mean())
data['Annual Income'] = data['Annual Income'].fillna(data['Annual Income'].mean())
data['Project evlaution /Completeion'] = data['Project evlaution /Completeion'].fillna(data['Project evlaution /Completeion'].mean())
data['Ticket Solving Managements '] = data['Ticket Solving Managements '].fillna(data['Ticket Solving Managements '].mean())
data['Behaviourial Competence'] = data['Behaviourial Competence'].fillna(data['Behaviourial Competence'].mean())
data['WorkLifeBalance'] = data['WorkLifeBalance'].fillna(data['WorkLifeBalance'].mean())
data['TrainingTime(months)'] = data['TrainingTime(months)'].fillna(data['TrainingTime(months)'].mean())
data['Experience'] = data['Experience'].fillna(data['Experience'].mean())
data['RelationshipSatisfaction'] = data['RelationshipSatisfaction'].fillna(data['RelationshipSatisfaction'].mean())
data['JobSatisfaction'] = data['JobSatisfaction'].fillna(data['JobSatisfaction'].mean())
data['Job Level'] = data['Job Level'].fillna(data['Job Level'].mean())
data['JobInvolvement'] = data['JobInvolvement'].fillna(data['JobInvolvement'].mean())
data['environment satisifaction'] = data['environment satisifaction'].fillna(data['environment satisifaction'].mean())
data['position'] = data['position'].fillna(data['position'].mean())
data['department'] = data['department'].fillna(data['department'].mean())
data['On time Delivery'] = data['On time Delivery'].fillna(data['On time Delivery'].mean())
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data[['JobInvolvement', 'Feedbacks ', 'Experience',
  'Ticket Solving Managements ', 'On time Delivery',
  'environment satisifaction',
  'Psycho-Social Indicators', 'TrainingTime(months)',
  'JobSatisfaction','Workign hrs ','Project evlaution /Completeion']],
    data['Performance Rating'])

model = Sequential()
model.add(Dense(input_dim=data[
    ['JobInvolvement', 'Feedbacks ', 'Experience','Ticket Solving Managements ', 'On time Delivery','environment satisifaction',
    'Psycho-Social Indicators', 'TrainingTime(months)','JobSatisfaction','Workign hrs ','Project evlaution /Completeion']].shape[1], units=3, activation='relu'))
model.add(Dense(input_dim=data[
    ['JobInvolvement', 'Feedbacks ', 'Experience', 'Ticket Solving Managements ', 'On time Delivery',
     'environment satisifaction',
     'Psycho-Social Indicators', 'TrainingTime(months)', 'JobSatisfaction', 'Workign hrs ',
     'Project evlaution /Completeion']].shape[1], units=3, activation='relu'))
model.add(Dense(input_dim=data[
    ['JobInvolvement', 'Feedbacks ', 'Experience', 'Ticket Solving Managements ', 'On time Delivery',
     'environment satisifaction',
     'Psycho-Social Indicators', 'TrainingTime(months)', 'JobSatisfaction', 'Workign hrs ',
     'Project evlaution /Completeion']].shape[1], units=3, activation='relu'))
model.add(Dense(units=1, activation='relu'))
model.compile(optimizer='adam', loss=keras.losses.mean_absolute_error, metrics=['mae'])
model.fit(x_train, y_train, batch_size=10, epochs=13)
pred = model.predict([[x_test]])
#print(pred)
from sklearn.metrics import r2_score
abc=r2_score(y_test,pred)
print(abc)
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:53:47 2020

@author: deniz
"""

'''
True Negative = Algorithm predicted negative and its negative
True Positive = Algorithm predicted Positive and its Positive
False Positive = Algorithm predicted Positive and its negative
False negative =  Algorithm predicted negative and its Positive
'''

'''
Accuracy  = (TN+TP)/(TP+TN+FP+FN) Doğru Tahmin Edilen Tüm Değerler/ Tüm Değerler.
Bize Sınıflandırmamızın Ne Kadar Doğru Olduğunu Söyler

Recall=(TP)/(TP+FN) Doğru Tahmin Edilen Pozitif Değerler / Doğru Positive + Yanlış Negatif.
Accuracy Her Zaman Doğru Vermeyebilir.Yaz Gününde Yerde 3m Kar Olup Olmayacağını Tahmin Edecek Bir Algoritma 
Yazdığımızda Her Değeri Negatif Vermek Bizi Bilge Yapmaz Bu Yüzden Doğru Pozitif Değerler Üzerine Yoğunlaşır
(Dataya Göre Değişiklik Gösterebilir)

precision =(TP)/(TP+FP) Makinenin Doğru Tahmin Ettiği Tüm Pozitif Değer / Tüm Pozitif Tahminler
20 tane pozitif tahmin yaptıysa ve 10 tanesi doğru ise 0.5 olarak kabul edilir.Negatif Tahminler 
Önemsenmez

F1 score is the harmonic mean of precision and recall. The harmonic mean of a group of numbers
is a way to average them together. The formula for F1 score is below:
    
    F1=2*(recall*precision)/(recall+precision)
     
     
'''

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(labels)):
    if labels[i]==1 and guesses[i]==1:
        true_positives+=1
    
    if labels[i]==0 and guesses[i]==0:
        true_negatives+=1
    
    if labels[i]==0 and guesses[i]==1:
        false_positives+=1#Guesses = 1 but it is false
    
    if labels[i]==1 and guesses[i]==0:
        false_negatives+=1#Guesses = 0 but it is false
        
        
accuracy = (true_negatives+true_positives)/(true_positives+true_negatives+false_positives+false_negatives)
print('Accuracy :',accuracy)       
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
print(accuracy_score(labels,guesses))#accuracy function


recall = (true_positives)/(true_positives+false_negatives)
print('Recall :',recall)
print(recall_score(labels,guesses))


precision = (true_positives)/(true_positives+false_positives)
print('Precision :',precision)
print(precision_score(labels,guesses))


f_1=2*(recall*precision)/(recall+precision)
print('F1 :',f_1)


print(f1_score(labels, guesses, average=None))
print(f1_score(labels, guesses, average='macro'))
print(f1_score(labels, guesses, average='micro'))
print(f1_score(labels, guesses, average='weighted'))


 
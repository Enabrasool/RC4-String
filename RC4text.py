# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:20:10 2020

@author: Enab
"""
#KeyScheduling Algorithm. The Size of S-Vector is Taken to be 256 bytes. This means Key-stream is Generated of this Size Only. Key needs to be of any Size Lesser than this Ofcourse. Then We enter Our plain Text of Any Number of Characters. 
PlainText=[]
Key=[]
DecryptingText=[]
Val=input(" Enter String ")
for c in Val:
    PlainText.append(c)
Val=input("Enter Key ")
for c in Val:
    Key.append(c)
CipherText=[]
#Generating S-Vector and T-vector. Here we consider Size of keystream-T to be 8 instead of 256. Sizes of  S-vector and T-vector are Same  
T=[]
S=list(range(0,256))
j=0
i=0
while i < 256:
    while j < len(Key): 
        T.append(Key[j])
        j=j+1
        i=i+1
    
    j=0
#Pseudo-Random Number Generation
j=0
i=0
while i < 256:
 j=((j+S[i]+ord(T[i])) % 256 )
 S[i],S[j]=S[j],S[i]
 i=i+1
#Generating The Cipher Text Now
i=0
j=0
count=1
print(len(PlainText))
while i<len(PlainText):
    i=((i+1) % 256) 
    j=((j+S[i]) % 256) 
    S[i],S[j]=S[j],S[i]
    K=((S[i]+S[j]) % 256)
    x=S[K]
    CipherText.append(chr((ord(PlainText[i-1])) ^ (x)))
    print("count ",count,CipherText[i-1])
    count+=1
print('Ciphertext = ',(CipherText))


#Generating The PlainText
print('\n----------------------------------Decryption------------------------------\n')
count=0
i=0
S=list(range(0,256))
j=0
i=0
while i < 256:
 j=((j+S[i]+ord(T[i])) % 256 )
 S[i],S[j]=S[j],S[i]
 i=i+1
i=j=0
while i<len(PlainText):
    i=((i+1) % 256) 
    j=((j+S[i]) % 256) 
    S[i],S[j]=S[j],S[i]
    K=((S[i]+S[j]) % 256) 
    x=S[K]
    p=ord(CipherText[count])
    DecryptingText.append(chr((p) ^ (x)))
    count+=1   
print('DeCiphered Text',DecryptingText)  

      
   
    

    
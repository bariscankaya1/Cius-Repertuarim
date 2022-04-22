# coding=utf-8
import firebase_admin
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('cius-repertuar-firebase-adminsdk-ot70r-4e57dcded1.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':"https://cius-repertuar-default-rtdb.firebaseio.com/"
    })
ref=db.reference("/turkuler")
jsonData={
    "id":1,
    "isim":"Acem Kızı",
    "soz":"""Çırpınıp Da Şan Ovaya Çıkınca
Eğlen Şan Ovada Gal Acem Gızı.
Uğrun Uğrun Gaş Altından Bakınca
Can Telef Ediyor Gül Acem Gızı.

Seni Seven Oğlan Neylesin Malı,
Yumdukça Gözünden Döker Mercanı.
Burun Fındık Ağzı Gahve Fincanı,
Şeker Mi, Şerbet Mi Bal Acem Gızı.""",
    "nota":"https://www.turkuler.com/notalar/acemgizi.gif"
    }
ref.push(jsonData)
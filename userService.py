from flask import Flask 
import random
class userService:
  
  def generateSerialNumber(self) :
    index = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    x = ''
    for y in range(4) :
      for z in range(4) :
        x = x + random.choice(index)
        z
      else :
        if y in range(3) :
          x = x + "-"
    else : 
      return x
            
  def checkUsername (self) :
    for x in self.data :
      if self.username == self.data[x]["username"] :
        return 1
    return 0

  def checkPassword (self) :
    for x in self.data :
      if self.password == self.data[x]["password"] :
        return 1
    return 0

  def login (self) :
    if self.checkUsername() == 1 and self.checkPassword() == 1 :
      return 1
    else : return 0


  def __init__ (self,username,password) :
    self.username = username
    self.password = password
    self.data = {
      "admin" : {
        "username" : "admin",
        "password" : "12345"
      },

      "superadmin" : {
        "username" : "superadmin",
        "password" : "12345",
      },
    }
    self.food = {
      "admin" : {
        "food_name" : ["Nasi Goreng" , "Magelangan" , "Indomie Goreng" , "Nasi telor"],
        "food_price" : [10000 , 9000, 8000, 7000],
        "food_image" : [
            "annie-spratt-oT7_v-I0hHg-unsplash.jpg",
            "artem-beliaikin-cVqU6I87fjQ-unsplash.jpg",
            "sisko-afnindar-DEi2lb48EQc-unsplash.jpg",
            "markus-winkler-Fc4wTAhoKaw-unsplash.jpg" 
        ]
      },

      "superadmin" : {
        "food_name" : ["Burger" , "Pizza" , "Spagetti"],
        "food_price" : [15000 , 30000, 10000],
        "food_image" : [
          "ilya-mashkov-mkVa2hLJgnI-unsplash.jpg",
          "aurelien-lemasson-theobald-x00CzBt4Dfk-unsplash.jpg",
          "amirali-mirhashemian-v2z6Yhp_6Gc-unsplash.jpg"
        ]
      }
    }
    self.drink = {
        "admin" : {
        "drink_name" : ["Es teh" , "Es Jeruk" , "Kopi" , "Susu"],
        "drink_price" : [2000 , 3000, 4000, 5000],
        "drink_image" : [
            "blake-wisz-X6aY_j6JD_Y-unsplash.jpg",
            "daisy-lin-z6hbN1t60q4-unsplash.jpg",
            "jason-wong-kSlL887znkE-unsplash.jpg",
            "thomas-vimare-7ZkoxdZLrog-unsplash.jpg" 
        ]
      },

      "superadmin" : {
        "drink_name" : ["Dalgona Coffee", "Capucino Coffee"],
        "drink_price" : [8000, 9000],
        "drink_image" : [
          "isabela-kronemberger-FEZ3LXJ9uAY-unsplash.jpg",
          "fahmi-fakhrudin-nzyzAUsbV0M-unsplash.jpg"
        ]
      }
    }
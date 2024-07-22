import copy
import sqlite3
conn=sqlite3.connect('Dominos.db')
cursor=conn.cursor()
#cursor.execute('CREATE TABLE USER(UN VARCHAR(10),PWD VARCHAR(18),EMAIL VARCHAR(30))')
#cursor.execute('INSERT INTO USER VALUES("TAJ123","1920","taj65815@gmail.com")')

class Dominos:
   menu = [
    {'id':1,'name': "Margherita Pizza", "price": [99,199,399]},
    {'id':2,'name': "Pepperoni Pizza", "price": [169,309,499]},
    {'id':3,'name': "Vegetarian Pizza", "price": [119,299,399]},
    {'id':4,'name': "Hawaiian Pizza", "price": [349,425,498]},
    {'id':5,'name': "BBQ Chicken Pizza", "price": [390,449,529]},
    {'id':6,'name': "Meat Lovers Pizza", "price": [199,299,499]},
    {'id':7,'name': "Supreme Pizza", "price": [229,499,699]}]
   coke=[
    {'id':8,"name": "Coca Cola", "price": 90},
    {'id':9,"name": "Sprite", "price": 50},
    {'id':10,"name": "Fanta", "price": 30},
    {'id':11,"name": "Root Beer", "price": 90.9}]
   def __init__(self):
      self.cart=[]
      self.signed=False
      self.log=False
      self.Dominos_menu()
   def Dominos_menu(self):
      while True:
         print('-----------Welcome to Dominos---------\n')
         print('Enter 1: signup')
         print('Enter 2: Login')
         print('Enter 3: Logout')
         if self.log==True:
            print('Enter 4: Order')
            print('Enter 5: Open Cart')
            print('Enter 6: Display Bill')
            print('Enter 7: Remove Items')
         choice=int(input('Enter your choice: '))
         if choice==1:
            self.signup()
         elif choice==2:
            self.login()
         elif choice==3:
            self.logout()
            break
         elif choice==4:
            self.order()
         elif choice==5:
            self.open_cart()
         elif choice==6:
            self.disp_bill()
         elif choice==7:
            self.edit_cart()
            
         a=input('Do you want to continue (y/n): ')
         if a.lower()=='y':
            continue
         else:
            break
   def signup(self):
      if self.signed==False:
         e=l=list(cursor.execute('SELECT EMAIL FROM USER'))
         l=list(cursor.execute('SELECT UN FROM USER'))
         while True:
            email=input('Enter your email: ')
            if (email,) not in e:
               un=input('Enter your username: ')
               if (un,) not in l:
                  while True:
                     pwd1=input('Enter your password: ')  
                     pwd2=input('Confirm your password: ')
                     if pwd1==pwd2:
                        cursor.execute(f'''INSERT INTO USER VALUES("{un}","{pwd1}","{email}")''')
                        conn.commit()
                        print('Signup Successful\n')
                        self.signed=True
                        break
                     else:
                        print("Password doesn't match\n")
               else:
                  print('Username Unavailable\n')
                  continue
            else:
               print('Email already Exist\n') 
               continue
            break
      else:
         print('Already signed up...\n')
            
   def login(self):    
      e=list(cursor.execute('SELECT EMAIL FROM USER'))
      u=list(cursor.execute('SELECT UN FROM USER'))
      print('Enter 1: Login with Email..')
      print('Enter 2: Login with User Name..\n')
      choice=int(input('Enter your choice: '))
      if choice==1:    
         email=input('Enter your email: ')
         pwd=input('Enter your password: ')
         if (email,) in e:
               if (pwd,) in list(cursor.execute(f'SELECT PWD FROM USER WHERE EMAIL="{email}"')):
                  print('Login successful')
                  self.log=True 
               else:
                  print('Incorrect Password')
                  self.login()
                     
         else:
            print('Your email does not exist\n')
            n = input('Do you want to sign up y/n: ')
            if n.lower() =='y':
               self.signup()
            else:
               print('Have a nice day!!')
            

      elif choice==2:
            un=input('Enter your User name: ')
            pwd=input('Enter your password: ')
            if (un,) in u:
               if (pwd,) in list(cursor.execute(f'SELECT PWD FROM USER WHERE UN="{un}"')):
                  print('Login successful\n')
                  self.log=True
               else:
                  print('Incorrect Password')
                  self.login()
            else:
               print('Your username does not exist\n')
               n = input('Do you want to sign up y/n: ')
               if n.lower() =='y':
                  self.signup()
               else:
                  print('Have a nice day!!')
      else:
         print('Invalid choice\n')
         self.login()

   def logout(self):
      self.log=False
      print('Logout Successful')
   
   def order_coke(self):
      for i in Dominos.coke:
         l = len(str(i['id']))+len(i['name'])+4
         print(i['id'],'--',i['name'],' '*(20-l),i['price'],' Rs.')
      choice=int(input('Enter your choice: '))
      if choice in [8,9,10,11]:
         qty=int(input('Enter coke Quantity: '))
         for j in Dominos.coke:
            if j['id']==choice:
               for k in self.cart:
                  if k['id']==j['id']:
                     k['Quantity']+=qty
                     k['price']+=(j['price'])*qty
                     break
               else:
                  self.cart.append(copy.deepcopy(j))
                  self.cart[-1]['Quantity']=qty
                  self.cart[-1]['price']=(j['price'])*qty
                  self.cart[-1]['cat']='   '
         print('Item Added to your cart...\n')
         ch=input('Do you want to add more...? (Type: y/n): ')
         if ch.lower()=='y':
            self.order()
      else:
         print('Invalid choice ... please Enter valid choice\n')
         self.order_coke()
         
   
      
   def order_pizza(self):
      print('         Item         ','      Regular    ','Medium    ','Large    ')
      print('         ____         ','      _______    ','______    ','_____    ')
      for i in Dominos.menu:
         l = len(str(i['id']))+len(i['name'])+4
         print(i['id'],'--',i['name'],' '*(25-l),'--',i['price'][0],'Rs.   ',i['price'][1],'Rs.   ',i['price'][2],'Rs.')
      choice=int(input('Enter your choice: '))
      if choice in [1,2,3,4,5,6,7]:
         print('Enter 1: Regular')
         print('Enter 2: Medium')
         print('Enter 3: Large')
         ch=int(input('Enter your choice: '))
         l = ['Reg','Med','Lar']
         qty=int(input('Enter Pizza Quantity: '))
         for i in Dominos.menu:
            if i['id'] == choice: 

               for j in self.cart:
                  if  i['id']==j['id'] and l[ch-1] == j['cat']:
                     j['Quantity']+=qty
                     j['price']+=(i['price'][ch-1])*qty
                     break
               else:
                  self.cart.append(copy.deepcopy(i))
                  self.cart[-1]['Quantity']=qty
                  if ch==1:
                     self.cart[-1]['price']=(i['price'][0])*qty
                     self.cart[-1]['cat']='Reg'
                  elif ch==2:
                     self.cart[-1]['price']=(i['price'][1])*qty
                     self.cart[-1]['cat']='Med'
                  elif ch==3:
                     self.cart[-1]['price']=(i['price'][2])*qty
                     self.cart[-1]['cat']='Lar'
                  else:
                     print('Invalid choice')
                     self.order_pizza()

         print('Item Added to your cart...\n')
         ch=input('Do you want to add more...? (Type: y/n): ')
         if ch.lower()=='y':
            self.order()
      else:
         print('Invalid choice ... please Enter valid choice\n')
         self.order_pizza()

   
   def order(self):
      if self.log==True:
         print('Enter 1: order Pizza\'s')
         print('Enter 2: order Cokes\n')
         ch=int(input('Enter your choice: '))
         if ch==1:
            self.order_pizza()
         elif ch==2:
            self.order_coke()
         else:
            print('Invalid choice\n')
            self.order()
      else:
         print('Login Required....\n')
         self.login()

   def open_cart(self):
      if self.log==True:
         print('---------------------Your CART----------------------')
         print('         Item     ','             Qty    ','    Price    ')
         print('         _____    ','             ___    ','    _____')
         for i in self.cart:
            l = len(str(i['id']))+len(i['name'])+4
            print(i['id'],'--',i['name'],' '*(25-l),f'({i['cat']})',i['Quantity'],'--------',round(i['price'],3),'Rs.')
      else:
         print('Login Required....\n')
         self.login()
   
   def edit_cart(self):
      if self.log==True:
         self.open_cart()
         if self.cart!=[]:
            choice=int(input('Enter your choice: '))
            if choice in [1,2,3,4,5,6,7]:
               print('Enter 1: Regular')
               print('Enter 2: Medium')
               print('Enter 3: Large')
               cat=int(input('Enter category: '))
            l=['Reg','Med','Lar']
            qty=int(input('Enter Quantity to remove: '))
            if qty>0:
               for j in self.cart:
                  if j['id']==choice and (j['cat']=='   ' or j['cat']==l[cat-1]):
                     if qty>j['Quantity']:
                        print('Quantity you entered is greater')

                     elif  qty<j['Quantity']:
                        j['price']-=(j['price']/j['Quantity'])*qty
                        j['Quantity']-=qty
                        print(qty,'Item\'s removed...')

                     else:
                        self.cart.remove(j)
                        print(qty,'Item\'s removed...')
                     break

               else:
                  print('Item is not present in your cart...')
            else:
               print('No items removed Enter quantity greater than zero')
         else:
            print('Your cart is Empty...')
         
         a=input('Do you want to remove more (y/n): ')
         if a.lower()=='y':
            self.edit_cart()
      else:
         print('Login Required....\n')
         self.login()


   def disp_bill(self):
      if self.log==True:
         amt=0
         qty=0
         print('--------------------DOMINOS PIZZA----------------------')
         print('------------------------BILL---------------------------')
         print('     Item     ','             Qty    ','    Price    ')
         print('     _____    ','             ___    ','    _____\n')
         for i in self.cart:
            l = len(str(i['id']))+len(i['name'])+4
            print(i['name'],' '*(25-l),f'({i['cat']})',i['Quantity'],'--------',i['price'],' Rs.')
            amt+=i['price']
            qty+=i['Quantity']
         print('Total :  ',' '*17,qty,'--------',round(amt,3),' Rs.\n')
      else:
         print('Login Required....\n')
         self.login()

ob=Dominos()

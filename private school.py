from prettytable import PrettyTable

 ###  class Courses
class Courses:                                                   
                                                                  
    no_of_use=0                                                                 

    def __init__(self, column_1, column_2, column_3, column_4, column_5 ):    
       self.column_1 =  column_1
       self.column_2 = column_2
       self.column_3 = column_3
       self.column_4 = column_4
       self.column_5 = column_5
       Courses.no_of_use+=1


    def __str__(self):
        return f"Νεα καταχωριση στην:{self.column_2}!!!! "               

 ### Method of the class Courses
    @classmethod                                                         
    def how_many(cls):
        return cls.no_of_use 


## array and demo data

x = PrettyTable(["Course Title", "Course Language", "Course Description", "Course Type "])  
x.add_row(["CB13FTPY", "Python", "Python 12 weeks", "Full Time"])
x.add_row(["CB13FTjY", "Java", "Java  12 weeks", "Full Time"])
x.add_row(["CB13FTCY", "C# ", "C#  12 weeks", "Full Time"])
        


y = PrettyTable(["First Name", "Last Name ", "Subject"])                               
y.add_row(["Dimitris", "zois","Python"])
y.add_row(["Dimitris", "Giannakopoulos", "Java "])
y.add_row(["Stamatis", "Sideris", "C#  "])


                                                                        
z = PrettyTable(["First Name", "Last Name", "Day of Birth", "Tution Fess ","Course"])       
z.add_row(["Giannis", "Pantelakis", "12/03/1990", "25000 $","python"])
z.add_row(["Aggelos", "Lykoudis","06/11/1988", "3000 $","java"])
z.add_row(["Ioannis", "Nikolaou", "19/06/1988", "3000 $","c#"])
z.add_row(["Giorgos", "Oikonomakis ", "15/09/1991", "25000 $","java"])


r = PrettyTable(["Title", "Description", "Date of Submission", "Mark for the Submitted Code ","Mark for the Oral Mark"])     
r.add_row(["Brief", " Python ", "12/05/2021", "60/100","40/100"])
r.add_row(["Private School", " Java","19/04/2021", "60/100","40/100"])
r.add_row(["calculato", " c#", "17/04/2021", "60/100","40/100"])
r.add_row(["Cesar", " Java", "10/04/2021", "60/100","40/100"])

studens_python = PrettyTable(["First Name", "Last Name "])         
studens_python.add_row(["Giannis", "Pantelakis"])
studens_python.add_row(["Ioannis", "Nikolaou"])


studens_java = PrettyTable(["First Name", "Last Name "])           
studens_java.add_row(["Aggelos", "Lykoudis"])
studens_java.add_row(["Giorgos", "Oikonomakis"])

studens_c = PrettyTable(["First Name", "Last Name "])                
studens_c.add_row(["Ioannis", "Nikolaou"])

trainer_python = PrettyTable(["First Name", "Last Name "])             
trainer_python.add_row(["Dimitris", "zois"])


trainer_java = PrettyTable(["First Name", "Last Name "])       
trainer_java.add_row(["Dimitris", "Giannakopoulos"])

trainer_c = PrettyTable(["First Name", "Last Name "])
trainer_c.add_row(["Stamatis", "Sideris"])

assignments_python= PrettyTable([ "Title Assignments"])
assignments_python.add_row(["Brief"])


assignments_java= PrettyTable([ "Title Assignments"])
assignments_java.add_row(["Private School"])
assignments_java.add_row(["Cesar"])

assignments_c= PrettyTable([ "Title Assignments "])
assignments_c.add_row(["calculato"])

 
studens_Pantelakis = PrettyTable([ "Course","Title Assignments "])          
studens_Pantelakis.add_row(["Python ","Brief"])

studens_Lykoudis = PrettyTable([ "Course","Title Assignments "])
studens_Lykoudis.add_row(["java ","Private School"])
studens_Lykoudis.add_row(["java ","Cesar"])

studens_Oikonomakis = PrettyTable([ "Course","Title Assignments "])
studens_Oikonomakis.add_row(["java ","Private School"])
studens_Oikonomakis.add_row(["java ","Cesar"])


studens_Nikolaou = PrettyTable([ "Course ","Title Assignments "])

studens_Nikolaou.add_row(["Python ","Brief"])
studens_Nikolaou.add_row(["C# ","calculato"])

studens_coursers = PrettyTable(["First Name", "Last Name "])                          
studens_coursers.add_row(["Ioannis", "Nikolaou"])


####  the main  menu #####

menu =   """1) Courses                           
2)Trainer
3)Studens 
4)Assignments
5)Αν θες να δεις ανα Cousers τους Trainer τους Studens και τις Assignments
6)Αν θες να δεις ολες τις Assignments που εχει ο καθε Studens ανα Courses
7)Αν θες να δεις ολους τους Studens που εχουν πανω απο ενα Courses
8)Εξοδος
"""





####  main  
while True:
    print(menu)                                                                  
    choice = int(input("Δωσε ενα αριθμο  αναλογα με το τι που ψαχνεις:"))

    if choice not in range(1,8):
        print("Επιλεξατε εναν αριθμο απο το 0 ως το 8 ")    

        ### courses  menu ####
    if choice ==1:                                                                                
        menu1="""        1)Πατα 1 αν θες να σου  εμφανιστει ολη η λιστα των Course                   
        2)Πατα 2 να για προθεσεις νεω Course
        3)Πατα 3 για πας στο αρχικο menu""" 
        
        while True:
        # shows us the options we have in Courses menu
            print(menu1)                                                                                 
            choice_Courses = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))
            # correct choice check
            if choice_Courses not in range(1,3):       
                                                                     
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 3 ")                                            
                print("_"*100)

            if choice_Courses == 3 :   
                break                                                                     
                
             ### Printing the list of Courses
            if choice_Courses == 1:                                                        
                print(x) 
                print("_"*100)        

            #  create new Course
            if choice_Courses == 2:
                new = input("Δωσε Course Title: ")                                                            
                new1 = input("Δωσε Course Language: ")
                new2 = input("Δωσε Course Description: ")
                new3 = input("Δωσε Course Type: ")

                ### create an object of the class Cources
                courses1 = Courses(new, new1, new2, new3, 0)  
                                                          
                print(courses1)    
                #### add the new data to the array                                                                    
                x.add_row([courses1.column_1,courses1.column_2,courses1.column_3, courses1.column_4])     
                ### print new array                                                                            
                print (x)                                                                                  
                 
                

                ### print the class method
                if Courses.no_of_use >1 :                                                              
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεες καταχωρισεις")
                else :
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεα καταχωριση")
                print("_"*100)    

                

            ### exit to loop
            if choice_Courses == 3:                                                              
                break

             ###  Trainer menu ####
  
    if choice == 2:
        menu2="""        1)Πατα 1 αν θες να σου εμφανιστουν ολoι οι  Trainer                  
        2)Πατα 2 να για προθεσεις νεω Trainer
        3)Πατα 3 για πας στο αρχικο menu""" 

        while True:
            # shows us the options we have in Trainer menu 
            print(menu2)
            choice_Trainer = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))

            if choice_Trainer not in range(1,3):                                                             
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 3 ")                                           
                print("_"*100)
               
            if choice_Trainer == 1: 
                print(y)

            #  create new  Trainer
            if choice_Trainer == 2:

                newW = input("Δωσε First Name: ")                                                            
                newW1 = input("Δωσε Last Name: ")
                newW2 = input("Δωσε Subject: ")

                
                trainer1 = Courses(newW, newW1, newW2, 0, 0)                                             
                print(trainer1)                                                                           
                y.add_row([trainer1.column_1,trainer1.column_2,trainer1.column_3, ])                      
                print (y)                                                                                     

               # checks the data user has given us and registers it in the appropriate courses  per trainer array
                if len(newW2)  == 6:                                                                       
                    trainer_python.add_row ([trainer1.column_1, trainer1.column_2 ])                        
                     
                elif len(newW2)  == 4 :                                                                          
                    trainer_java.add_row ([trainer1.column_1, trainer1.column_2 ])                              
                                                                                                                 
                else:
                    trainer_c.add_row ([trainer1.column_1, trainer1.column_2 ])
                         

                if Courses.no_of_use >1 :
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεες καταχωρησεις")                      
                else :
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεα καταχωρηση")
                print("_"*100)   

                
                
           ### exit to loop       
            if choice_Trainer == 3:
                break 


               ###  Studens menu ####

    if choice == 3:


        menu3="""        1)Πατα 1 αν θες να σου εμφανιστουν ολα τα Studens                   
        2)Πατα 2 να για προθεσεις νεω Studens
        3)Πατα 3 για πας στο αρχικο menu""" 


        while True:
            # shows us the options we have in Studens  menu
            print(menu3)
            choice_Studens = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))

            if  choice_Studens not in range(1,3):                                                             
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 3 ")                                           
                print("_"*100)
               
            if  choice_Studens == 1: 
                print(z)
        
            #  create new Studen
            if choice_Studens == 2:

                news = input("Δωσε First Name: ")                                                            
                news1 = input("Δωσε Last Name: ")
                news2 = input("Δωσε Day of Birth: ")
                news3 = input("Δωσε Tution Fess: ")
                news4 = input("Δωσε courses: ")
                ### create an object of Studen
                studens1 = Courses(news, news1, news2, news3, news4)                                                              
                print(studens1)                                                                                                    
                z.add_row([studens1.column_1, studens1.column_2, studens1.column_3, studens1.column_4, studens1.column_5 ])          
                print (z)                                                                                                               
            # checks the data user has given us and registers it in the appropriate courses per studens array
                if len(news4)  == 6:                                                                                              
                    studens_python.add_row ([studens1.column_1, studens1.column_2 ])                                               
                     
                elif len(news4)  == 4 :  
                    studens_java.add_row ([studens1.column_1, studens1.column_2 ]) 

                else:
                    studens_c.add_row ([studens1.column_1, studens1.column_2 ])


                if Courses.no_of_use >1 :                                                                                             
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεες καταχωρισεις")
                else :
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεα καταχωριση")
                print("_"*100)   
                
            ### exit to loop
            if choice_Studens == 3:                                                                                                      
                break 
        
                      ### Assignments menu ####
    if choice == 4:

        menu4="""        1)Πατα 1 αν θες να σου εμφανιστουν ολα τα Assignments                   
        2)Πατα 2 να για προθεσεις νεω Assignments
        3)Πατα 3 για πας στο αρχικο menu""" 

        while True:
            # shows us the options we have in Assignments menu
            print(menu4)                                                                                 
            choice_Assignments = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))

            if choice_Assignments not in range(1,3):                                                              
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 3 ")                                            
                print("_"*100)


            if  choice_Assignments == 1: 
                print(r)    

            if  choice_Assignments == 2:

                newss = input("Δωσε Title: ")                                                            
                newss1 = input("Δωσε Description: ")
                newss2 = input("Δωσε Date of Submission: ")
                newss3 = input("Δωσε Mark for the Submitted Code: ")
                newss4 = input("Δωσε Mark for the Oral Mark:")


                assignments1 = Courses(newss, newss1, newss2, newss3, newss4)                                                                                 
                print(assignments1)                                                                                                                                               
                r.add_row([assignments1.column_1, assignments1.column_2, assignments1.column_3, assignments1.column_4, assignments1.column_5 ])                    
                print (r)                                                                                                                                             

            # checks the data user has given us and registers it in the appropriate  Assignments  per studens array
                if len(newss1)  == 6:                                                                                                                                    
                    assignments_python.add_row ([assignments1.column_1 ])                                                                                                  
                     
                elif len(newss1)  == 4 :  
                    assignments_java.add_row ([assignments1.column_1 ]) 

                else:
                    assignments_c.add_row ([assignments1.column_1 ])    


                if Courses.no_of_use >1 :                                                                                  
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεες καταχωρισεις")
                else :
                    print(f"Εχει κανει μεχρι τωρα {Courses.no_of_use} νεα καταχωριση")
                print("_"*100) 

                

            if  choice_Assignments == 3:  
                break                                                                                                                                         

         ###  Studens per Courses, Trainers per Courses, Assignments per Courses  menu ####           
    if choice == 5:
        menu5="""        1)Πατα 1 αν θες να σου εμφανιστουν ολοι οι Studens ανα Courses                   
        2)Πατα 2 αν θες να σου εμφανιστουν ολοι οι Trainers ανα Courses  
        3)Πατα 3 αν θες να σου εμφανιστουν ολες οι Assignments ανα Courses
        4)Πατα 4 για πας στο αρχικο menu""" 

        while True:
            # shows us the options we have in Studens  menu
            print(menu5)                                                                                
            choice_per = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))
           #  correct choice check
            if choice_per not in range(1,4):                                                             
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 4 ")                                            
                print("_"*100)
            #### print all  Studens per Courses arrays
            if choice_per == 1:                                                                          
                print(f" οι Studens  που παρακολουθουν την Python :\n{studens_python}") 

                print(f" οι Studens  που παρακολουθουν την Java :\n{studens_java}")

                print(f" οι Studens  που παρακολουθουν την c# :\n{studens_c}")

            #### print all  Trainers per Courses arrays
            if choice_per == 2:                                                                               

                print(f" οι Trainers  που διδασκουν  στην Python :\n{trainer_python}")

                print(f" οι Trainers  που διδασκουν  στην Java :\n{trainer_java}")

                print(f" οι Trainers  που διδασκουν  στην C# :\n{trainer_c}")
             #### print all  Assignments per Courses arrays  
            if choice_per == 3:                                                                               
                print(f" οι Assignments  που εχουν δοθει  στην Python:\n{assignments_python}")

                print(f" οι Assignments  που εχουν δοθει  στην Java :\n{assignments_java}")

                print(f" οι Assignments  που εχουν δοθει  στην C# :\n{assignments_c}")
            ### exit to Studens per Courses, Trainers per Courses, Assignments per Courses  menu 
            if choice_per == 4:                                                                                              
                break    
        
                     ### Assignments per Courses menu 
    if choice == 6 :
        menu6="""        1)Πατα 1 αν θες να σου εμφανιστουν ολοι οι Studens με τις  Assignments που εχουν ανα Courses                  
        2)Πατα 2 για πας στο αρχικο menu""" 

        while True:
            print(menu6)                                                                                 
            choice_ava = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))

            if choice_ava not in range(1,2):                                                             
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 2 ")                                           
                print("_"*100)
            ### print all  Studens per Assignments arrays
            if choice_ava == 1:                                                                                  

                print(f" o Giannis Pantelakis  εχει τις παρακατω   Assignments :\n{studens_Pantelakis}")

                print(f" o Aggelos Lykoudis  εχει τις παρακατω   Assignments :\n{studens_Lykoudis}")

                print(f" o Giorgos Oikonomakis εχει τις παρακατω   Assignments :\n{studens_Oikonomakis}")

                print(f" o Ioannis ONikolaou εχει τις παρακατω   Assignments :\n{studens_Nikolaou}")

                
            if choice_ava == 2:                                                                                                    
                break  
                        ###  memu  studens that belong to more than one courses 
    if choice == 7 :
        menu7="""        1)Πατα 1 αν θες να σου εμφανιστουν ολοι οι Studens που παρακωλουθουν πανω απο 1 Courses                   
        2)Πατα 2 να για προθεσεις νεω  Studen
        3)Πατα 3 για πας στο αρχικο menu""" 

        while True:

            print(menu7)                                                                               
            choice_qwe = int(input("Δωσε ενα  αριθμο αναλογα με τη θες να κανεις:"))


            if choice_qwe not in range(1,2):                                                             
                print("Επιλεξατε εναν αριθμο απο το 0 ως το 2 ")                                           
                print("_"*100) 

            if choice_qwe == 1:                                                                                
                 print(studens_coursers)
            ##### makes a new entry in the table
            if choice_qwe == 2:                                                                                 

                newstu = input("Δωσε First Name: ")
                newstu1 = input("Δωσε Last Name: ")
               ### add new data in array studens per coursers
                studens_coursers.add_row([newstu, newstu1])
                print(studens_coursers)                                                                                      


          ### exit the menu
            if choice_qwe == 3:                                                                           
                break      


# exit the program
    if choice== 8:
        break                                                                                   
import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ra1190@cm",
  database="Spottabl"
)

def getData(query):
    mycursor= mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


query1="SELECT COUNT(email) FROM registrations where email like '%spottabl'; "
query2="SELECT COUNT(email) FROM registrations where email like '%flexmoney.in'; "
query3="SELECT COUNT(email) FROM clientuserinvites where inviter like '%spottabl%' and clientcode='flexmoney'; "
query4="SELECT COUNT(email) FROM clientuserinvites where inviter like '%spottabl%' and clientcode='Spottabl'; "
query5="SELECT COUNT(email) FROM clientuserinvites where accepted='true' and clientcode='Spottabl'; "
query6="SELECT COUNT(email) FROM clientuserinvites where accepted='true' and clientcode='flexmoney'; "

Number_of_users_on_spottabl_spottabl=getData(query1)
Number_of_users_on_spottabl_flexmoney=getData(query2)
Number_of_users_invited_from_spottabl_flexmoney=getData(query3)
Number_of_users_invited_from_spottabl_spottabl=getData(query4)
Number_of_users_who_have_accepted_invite_spottabl=getData(query5)
Number_of_users_who_have_accepted_invite_flexmoney=getData(query6)



fields = ['clientcode', 'Number of users on spottabl', 'Number of users invited from spottabl','Number of users who have accepted invite']
rows=[['Spottabl',Number_of_users_on_spottabl_spottabl[0][0],Number_of_users_invited_from_spottabl_spottabl[0][0],Number_of_users_who_have_accepted_invite_spottabl[0][0]]
      ,['flexmoney',Number_of_users_on_spottabl_flexmoney[0][0],Number_of_users_invited_from_spottabl_flexmoney[0][0],
        Number_of_users_who_have_accepted_invite_flexmoney[0][0]]]

filename = "Spottabl_data_results.csv"
with open(filename, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile)
     
    
    csvwriter.writerow(fields)
     

    csvwriter.writerows(rows)

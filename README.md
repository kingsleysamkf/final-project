# Clinic Inspection and Regulatory Record System
### Video Demo: <https://youtu.be/LkOVBj6YnyI> CS50xfinal_Sam King Fung .mp4
## Description: 
cs50x final project: Clinic Inspection and Regulatory Record System
This project is a web-based application to provide an electronic system for recording clinic inspection findings and regulatory actions issued to the clinic by regualatory body. It is designed for clinic inspectors of regulatory body who are required to conduct routine inspection in the healthcare facilities like clinics. The system provides an user interface to inspectors(user), when there is irregularity or area to be improved related to patient safety issue, inspector can record the information in the system after the inspection. The date is stored in SQL database which is easy for data analysis and data retrieval. 

### Technologies used:
It makes use of the JavaScript, Python, SQL and Flask as key elements of the technical basis. 

### How the webpage works?
The idea is simple. The key functions include register, login, logout, clinic profolio, inspection finding, history. There are tabs at the top of webpage for the those functions.

1. Register, Login and Logout:
New user is required to register to the webpage. Every user has his/her own unique user_id to register new user need to set up "username", "password" and reconfirm the "password".
User are required to login by using correct username and pasword.
When user need to leave the system, logout is required. 

2. Clinic profolio:
In real working enviornment, inspector is assigned to routinely perform inspection to a list of clinic which is under his/er purview. Therefore, in each user's account, the homepage only displays the clinic profolio that is handled by the user. A user is not able to view the clinic profolio of another user.

3. Inspection finding
User can input the information like clinic number, clinic name, inspection finding, inspection date and regulatory action taken to the clinic in the system.

4. History
User can view the history of the inspection finding and regulatory action taken of each clinic that was input previously.

### Datebase
There 3 database in SQL are used including " user", "record" and "profolio". 

### Possible improvements
1. Have administrator account to revise record and handle user account.
2. Email function can be added to allow user to send email to the clinic related to the inspection finding and regulatory action details.
3. Enrich the database by adding more columns to log more information in the system

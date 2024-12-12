# Clinic Inspection and Regulatory Record System
### Video Demo: <https://youtu.be/LkOVBj6YnyI> CS50xfinal_Sam King Fung .mp4
## Description: 
cs50x final project: Clinic Inspection and Regulatory Record System(CIRRS)

This project is a web-based application to provide an electronic system for recording clinic inspection findings and regulatory actions issued to the clinic by regulatory body. In the realm of public health, ensuring compliance with regulations and maintaining high standards in clinics is paramount. The web application designed for a Clinic Inspection and Regulatory Record System (CIRRS) can significantly enhance the efficiency and effectiveness of government inspectors tasked with overseeing healthcare facilities. 

CIRRS is designed for clinic inspectors of regulatory body who are required to conduct routine inspection in the healthcare facilities like clinics. The system provides an user interface to inspectors(user), when there is irregularity or area to be improved related to patient safety issues, inspector can record the information in the system after the inspection. The data is stored in SQL database which is easy for data analysis and data retrieval. This essay outlines the technologies used, the functions of the application, its limitations, and the database application that supports it.

### Technologies used:
The CIRRS leverages a combination of modern web technologies to create a robust and user-friendly platform. The primary technologies involved include JavaScript, Python, SQL and Flask as key elements of the technical basis. 

### How the webpage works?
The idea is simple. The key functions include "register", "login", "logout", "clinic profolio", "inspection finding" and "history". There are tabs at the top of the webpage for those functions.

1. Register, Login and Logout:
The system can manage user roles and permissions, allowing access for inspectors from different inspection teams in the office. This ensures that sensitive data is protected and only accessible to authorized personnel. New user is required to register to the webpage. Every user has his/her own unique user_id to register new users need to set up "username", "password" and reconfirm the "password". Users are required to login by using the correct username and pasword. When a user needs to leave the system, logout is required.

3. Clinic profolio
In a real working enviornment, an inspector is assigned to routinely perform inspection to a list of clinics which is under his/her purview. Therefore, in each user's account, the homepage only displays the clinic profolio that is handled by the user. A user is not able to view the clinic profolio of another user.

4. Inspection finding
Inspectors can enter inspection results directly into the system, including inspection finding regarding the compliance requirement, inspection date, and the official regulatory action taken. This feature allows for real-time data entry and reduces the reliance on paper records. User can input the information like clinic number, clinic name as unique identifier for the accurate documentation in the system. The CIRRS facilitate the data entry and management.

5. History
User can view the history of the inspection finding and regulatory action taken of each clinic that was input previously in the inspection finding function. 


### Datebase
The database application plays a critical role in the CIRRS, serving as the backbone for data storage and management. Clinic_number is the primary data shared by the 3 SQL database. There 3 database in SQL are used including " user", "record" and "profolio". 
1. User: Maintaining a list of inspectors, their credentials, and their assigned clinics.
2. Records: Keeping track of inspection finding of each inspection over time, and regulatory action taken in response to the finding. 
3. Profolio: Storing information about each clinic, including clinic number as unique identifier, clinic name, size of clinic quantified by the number of room, and type of medical services offered.
By utilizing SQL for data management, inspectors can efficiently query the database to retrieve specific records, generate reports, and analyze trends in clinic compliance.

### Possible improvements
1. Create an administrator account to revise records and handle user accounts and insert row in clinic profolio when there are new clinics in the future. 
2. Email function can be added to allow users to send email to the clinic related to the inspection finding and regulatory action details.
3. Enrich the database by adding more columns to record more information in the system.
4. As the number of clinics and inspections grows, the application must be able to scale accordingly. This may require additional resources and infrastructure to handle increased data loads and user traffic.


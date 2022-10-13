**Inner Intel (Web)**

[![](https://img.shields.io/badge/InnerIntel_Web-V1.0.0-blue.svg)]()  [![](https://img.shields.io/badge/Landing_Page-URL-green.svg)](https://personalisednutrition.github.io) 

---

> Web application for nutritionists

#### 01_Development background

The S.A.Y. team has developed Inner Intel, a Java-based app for Android.
After understanding the needs of nutritionists, the team decided to continue to develop an Inner Intel web-based application that would meet the needs of nutritionists to Contact and guide general users in dietetics.

---

#### 02_Technical selection

1. **System environment**
   - Windows
   - Ubuntu
   - Chrome
   
2. **Main framework**
   - Django
   - Firebase

---

#### 03_Main Features.

- Shared database with the Inner Intel java side serving regular users.
- There is a complete permission management system.
- There is a comprehensive privacy protection policy.

---

#### 04_Main Functions

- Allows visual viewing of user-specific data.
- The java side of the specified user can be set up by nutritionists.
- nutritionists can view the system's analysis of the specified user's data.
- nutritionists can upload data analysis reports from nutritionists.
- Allow nutritionists to log in using their account email.
-  The nutritionist can view the list of users, priorities, appointment dates, new information on the home page. and sorted by the above characteristics.
- The dietitian can view the user's details and select up to four of the automatically generated reports to display graphical data on the user's details page.
- The nutritionist can tag user data and set up reminder pushes.

---



#### 05_Development Plan

> If the Gantt chart doesn't display, please flash the page.

```mermaid
 gantt 
        dateFormat  MM-DD
        title Development Plan 
        section Preparation
        Work handover & Demand communication		:done,p0, 07-25,07-31
        Adjust demands                          	:done,p1, 07-31,08-08
        
        section Web Development 
        Front-end design                        	:done,d0,08-08,08-21
        prototype                                   :done,d1,08-13,08-21
        Back-end design(UML)						:done,d2,after d1,09-04
        Basic function								:done,d3,after d2,09-18
        Buffer Week									:done,d4,after d3,09-25
        Business logic development					:done,d5,after d4,14d
        Front-end and back-end docking & optimization :done,d6,after d5,7d
        
        section Database Development 
        Database Development_01						:done,dd0,08-08,09-18
        Buffer Week									:done,d4,after d3,09-25
        Database Development_02						:done,dd1,after d4,10-23
        
        section Data Collection
        Form creation								:done,c0,08-15,7d
        Form adjustment								:done,c1,after c0,7d
        Data collection								:done.c2,after c1,10-28
        Data Cleaning								:done,c3,09-19,14d
        
        section Test
        Interface testing and functional testing 	:t0,after d6,10-23
        
        section Handover
      	Work handover								:h0,after t0,10-28
```

---



#### 06_Routing path

- Index page：

  ```
  inner/login/  
  ```

- client page：

  ```
  inner/client/  
  ```

- message page：

  ```
  inner/message/  
  ```

- setting page：

  ```
  inner/setting/  
  ```

- client_data page：

  ```
  inner/client/data/  
  ```

- client_note page：

  ```
  inner/client/note/  
  ```

- client_profile page：

  ```
  inner/client/profile/  
  ```

- client_appointment page：

  ```
  inner/client/appointment/  
  ```

  ---



#### 07_API

> The API description will be updated in 12 week.

1. login page

| Interface path                           | inner/login/user/                                            |
| ---------------------------------------- | ------------------------------------------------------------ |
| Interface description                    | Users send their user email and password via the form for login verification. |
| Interface type                           | POST                                                         |
| Key_1                                    | email（Transfer of user login email）                        |
| Key_2                                    | pwd （Transfer of user login password）                      |
| Login Success Response                   | index.html Page                                              |
| User email password match error response | login.html   (error_msg = 'Wrong email or password')         |

2. index page

| Interface path        | inner/index/client_cid/                                      |
| --------------------- | ------------------------------------------------------------ |
| Interface description | When clicking on the user's avatar ，send uid of the current user to client page。 |
| Interface type        | GET                                                          |
| Key                   | cid（send id）                                               |
| Success Response      | client.html Page                                             |
| error response        | client.html Page（No user information displayed）            |

---



#### 08_Group S.A.Y. Team Members

| Name        | title                         | Email               |
| ----------- | ----------------------------- | ------------------- |
| Shuyi Chen  | Spokesperson, Project Manager | u7175274@anu.edu.au |
| Yuhao Zhai  | Spokesperson, Project Manager | u7152566@anu.edu.au |
| Xinyue Hu   | Database Manager              | u7151386@anu.edu.au |
| Hengtong Wu | Database Engineer             | u7235221@anu.edu.au |
| Tianqi Tang | Techinical Lead               | u7192230@anu.edu.au |
| Shiyun Zhu  | Web Developer                 | u7041419@anu.edu.au |
| Siyuan He   | Web Developer                 | u7344524@anu.edu.au |

---

#### 09_License

None

---

#### 

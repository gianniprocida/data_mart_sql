<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Overview</h1>
    <hr>The task is to create a database schema capable of efficiently storing, managing, and processing data pertaining to the use of Airbnb.
     <p> 
 </p>
    <h2>Getting started</h2>

   <h3>How to run it?</h3>
   <ul>
     <li>Clone the repository from GitHub: git clone https://github.com/gianniprocida/data_mart_sql</li>
     <li>Navigate to the data_mart_sql: cd data_mart_sql</li>
     <li>Install any dependencies required by the project:
      <ul>
          <li>numpy.</li>
          <li>pandas.</li>
          <li>mysql-connector-python.</li>
          <li>sqlalchemy.</li> 
      </ul>
     </li>
     <li>Run the fun.py script to generate the CSV files and prepare them for insertion into the respective tables.</li>
     <li>Execute the script createTable.sql to create tables in the data_mart_airbnb database. </li>
    <li>Run the PopulateTables.py. This script will handle the insertion of the CSV files into the corresponding table.</li>
    <li>Run the script addPK.sql to add a primary key to each table</li>
    <li>Execute the script addFK.sql to establish relationships between tables in the database.</li>
   </ul> 
   <h2> </h2>    
<h2>Conception phase</h2>
<img src="https://github.com/gianniprocida/data_mart_sql/blob/main/erd.png" height="700" width="1000">
Figure shows the physical data model that contains an excerpt of a model for our database 
regarding the Airbnb use case. The squares represent our entities and are filled with attribues associated with our
entities while the arrows between the squares indicate how the entities relate to one anothe
<h4>Relationships</h4>
<img src="https://github.com/gianniprocida/data_mart_sql/blob/main/relationships.png" height="500" width="400"/>
One-to-one: 
<ul>
    <li>A listing has one address</li>
    <li>A user has one address</li>
</ul>
One-to-many
<ul>
    <li>A user can write multiple reviews, but each review is associated with only one user.</li>
    <li>A listing can have multiple reviews associated with it, while each review can only be about one single listing.</li>
    <li>A user can write multiple messages, but each message is associated with only one user.</li>
    <li>A user can make multiple payments, while a payment can only be made by a single user.</li>
</ul>
Many-to-many
<ul>
    <li>A listing can have multiple amenities associated with it, and each amenity can be associated with 
    multiple listings.</li>
</ul>
</body>




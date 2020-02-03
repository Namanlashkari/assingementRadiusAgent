# assingementRadiusAgent
# author: Naman Lashkari



The following assingment can have atleast these three possible solution approaches.Also I took the libery to ponder upon 
a few future extension to the problem statement and how can be dealt while still resulting the best possible solution.

        
        1. SolutionApproach1:
              Technology stack: MySQL, Reddis, Flask, Python3.
              Softwares used: Pycharm, MySQl, MySql WorkBench.
              It has a locally hosted MySQL database which stores the database in a single table(could later be normalized 
              based on the requirements. Heavy queries can be implemented in geospatial queries )
                   
        2. SolutionAppraoch2:
              Technology stack: MySQL, Reddis, Flask, Python3.
              Softwares used: Pycharm, MySQl, MySql WorkBench.
              Implmenting the database using a Quadtree methodolgy for almost log(n) search retrival of best match enteries
              according to latitudes and longitutes.
              
              Extension to the idea:
              As the distance calculation is an memory intensive operation, we might further split the database using mutilple 
              tables/database to result in an efficient calultion and more optimail memorry allocation and the matching
              enteries can be matched leading to more optimized memory output and proper allocation of resources.  
         
        3. SolutioApprach3:
              Technology stack: Elastic search.
              Softwares used:
              Implementing the database using elatic search and optimizing most queries to produce almost ready to use 
              data. 
              
              Extension to the idea:
              1.The search can later be modified by introducting a criteria searching properities in a an area(every city
                might have at most 500 - 3000 sub societies/ region hence producing more indexable results.Out of 4 million 
                row
                rows of data in the database we can reduce the query to 50 thousand to 1 million queries in an region and can 
                can even reduced to a more precise result using indexing.
              
              
An later introdcution to the system architecture can be usage of spark to implement inbuild parallel processing capabilities 
of the same.
         
We can also implement batch processing to push notifications for customer when ever new properties are added to the database 
resulting in the increased customer involvement.

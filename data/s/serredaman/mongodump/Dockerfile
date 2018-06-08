FROM mongo  
MAINTAINER Eugene Lavrenchuk  
  
CMD mongodump -u 'superadmin' -p '12345' \--host
'mongo1:27017,mongo2:27017,mongo3:27017' \--out=/tmp  


FROM ubuntu:14.04.2  
MAINTAINER Adnan Issadeen <spartakode@outlook.com>  
  
RUN apt-get update && apt-get install wget curl sqlite3 nginx vim -y --force-
yes  
ADD nginxfile /etc/nginx/sites-available/newdefault  
RUN rm /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-
available/newdefault /etc/nginx/sites-enabled/newdefault  


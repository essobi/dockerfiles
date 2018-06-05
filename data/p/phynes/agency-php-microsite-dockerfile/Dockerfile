#Description: Generic Dockerfile for hosting php applications on apache  
#Date:07.10.15  
FROM php:5.6-apache  
  
#Author  
MAINTAINER "Patrick Hynes"  
#Install the dependecies (GIT)  
RUN apt-get update -y  
RUN apt-get install git -y  
  
#Setup the Environment Variables  
ENV gitrepo https://github.com/phyneswlgore/testphp-app.git  
ENV tag latest  
  
#Clean up the container  
RUN cd /var/www/html/  
RUN rm *  
  
#Clone the app to the necessary directory  
RUN git clone ${gitrepo} /var/www/html/  
  
#Expose port 80  
EXPOSE 80  


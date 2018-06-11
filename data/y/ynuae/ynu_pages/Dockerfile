# Set the base image to nginx  
FROM nginx  
  
# File Author / Maintainer  
MAINTAINER Liudonghua <liudonghua123@gmail.com>  
  
# update the repository sources list  
RUN apt-get update  
  
# install vim for quick modify  
RUN apt-get install -y vim  
  
# copy static resources to the specified location  
COPY html /usr/share/nginx/html  
  
# remove the index html to prevent index access  
RUN rm /usr/share/nginx/html/index.html  


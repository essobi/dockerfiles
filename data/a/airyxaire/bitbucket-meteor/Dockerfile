FROM node:latest  
  
# Add a user and a group called meteor  
RUN groupadd meteor && adduser --ingroup meteor --disabled-password --gecos ""
\--home /home/meteor meteor  
  
# Installing meteor  
USER meteor  
RUN curl https://install.meteor.com/ | sh  
  
# Linking meteor  
USER root  
RUN ln -s /home/meteor/.meteor/meteor /usr/local/bin/  
  
#set user to meteor  
USER meteor  


############################################################  
# Dockerfile to build Nginx Installed Containers  
# Based on Ubuntu  
############################################################  
  
# Use the latest official ubuntu base image from docker hub  
FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y nginx git curl python-software-properties python
software-properties-common  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
WORKDIR /opt/storefront  
RUN git clone https://ottemo-
dev:freshbox111222333@github.com/urbanityshop/storefront.git -b develop
/opt/storefront  
RUN npm update -g npm  
RUN npm install  
RUN npm install -g bower  
RUN bower install --allow-root  
RUN npm install -g gulp  
RUN gulp build  
RUN rm -f /etc/nginx/sites-enabled/default  
ADD ./config/storefront.conf /etc/nginx/conf.d/  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  


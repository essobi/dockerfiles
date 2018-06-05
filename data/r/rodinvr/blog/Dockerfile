FROM rodinvr/nodejs:6  
MAINTAINER Grigor Khachatryan <g@yvn.io>  
  
WORKDIR /var/www/admin  
  
ADD . /var/www/admin  
  
RUN npm install  
  
EXPOSE 5000  
CMD ["sh", "-c", "export NODE_ENV=test"]


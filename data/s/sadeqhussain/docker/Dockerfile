FROM ubuntu:latest  
MAINTAINER "Sadequl Hussain (sadeq68@yahoo.com)"  
RUN apt-get update -y && apt-get install nginx -y  
CMD service nginx start  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  


FROM ubuntu:14.04  
MAINTAINER mofon yzkf000@foxmail.com  
RUN apt-get update  
RUN apt-get install -y nginx  
COPY ./www /usr/share/nginx/html  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  


# Version: 0.0.1  
From ubuntu:14.04  
MAINTAINER secondhj "skatersecond@gmail.com"  
RUN apt-get update && apt-get install -y nginx  
RUN echo "Hi, I'm in your container" \  
> /usr/share/nginx/html/index.html  
RUN echo "</br>Automated Build Test" \  
>> /usr/share/nginx/html/index.html  
CMD nginx -g "daemon off;"  
EXPOSE 80  


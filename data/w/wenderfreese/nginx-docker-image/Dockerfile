# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Wender Freese "wender.jean@gmail.com"  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am your container' > /usr/share/nginx/html/index.html  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-g", "daemon off;"]  


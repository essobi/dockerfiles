# Version: 0.0.4  
FROM ubuntu:latest  
MAINTAINER Preston Davis "pwdavis@gmail.com"  
ENV REFRESHED_AT 2015_08_22  
RUN apt-get -qq update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am in your container v2' \  
>/usr/share/nginx/html/index.html  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-h"]  


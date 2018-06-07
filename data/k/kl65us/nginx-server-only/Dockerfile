# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER kl65us "efristical@gmail.com"  
ENV REFRESHED_AT 2016-03-30  
RUN apt-get update  
RUN apt-get install -y nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-g", "daemon off;"]  
EXPOSE 80  


FROM ubuntu:latest  
MAINTAINER Paolo Filippelli "paolo.filippelli@gmail.com"  
RUN apt-get update  
RUN apt-get install -yy nginx  
ADD index.html /usr/share/nginx/html  
EXPOSE 80  
# nginx parte in automatico  
ENTRYPOINT ["/usr/sbin/nginx"]  
  
# default params: modalità daemon off  
CMD ["-g", "daemon off;"]  


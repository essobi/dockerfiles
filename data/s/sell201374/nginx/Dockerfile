FROM ubuntu:14.04  
RUN apt-get update -y  
RUN apt-get install -y nginx curl git  
RUN rm -r /usr/share/nginx/html  
RUN git clone https://github.com/johnsonthomas1974/helloWorld.git
/usr/share/nginx/html/  
CMD ["/usr/sbin/nginx","-g", "daemon off;" ]  
# Expose ports.  
EXPOSE 80  


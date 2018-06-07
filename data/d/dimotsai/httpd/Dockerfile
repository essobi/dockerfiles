FROM ubuntu:latest  
MAINTAINER Chih-Hao Tsai <tsaichh@cs.nctu.edu.tw>  
RUN apt-get install -y apache2  
RUN echo "Hello Http" > /var/www/html/hello.txt  
EXPOSE 80 8080  
ENTRYPOINT ["/usr/sbin/apachectl", "-f", "/etc/apache2/apache2.conf", "-e",
"info", "-DFOREGROUND"]  
#CMD ["-D"]  


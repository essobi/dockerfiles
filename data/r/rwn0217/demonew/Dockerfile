FROM centos:latest  
MAINTAINER Raghu K "raghuk.vit@gmail.com"  
RUN yum install httpd -y  
#RUN echo Hello World > /var/www/html/index.html  
ADD index.html /var/www/html/index.html  
#ADD https://raw.githubusercontent.com/airpub/index.html/gh-pages/index.html
/var/www/html/index.html  
RUN chmod +r /var/www/html/index.html  
CMD /bin/bash -c "/usr/sbin/httpd -DFOREGROUND"  
EXPOSE 80  
ENV MYNAME=RAGHU  
ENV PORT=80  
ENV URL=localhost  


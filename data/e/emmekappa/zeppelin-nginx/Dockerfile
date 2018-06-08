FROM centos:centos7  
ENV ZEPPELIN_USER=zeppelin  
ENV ZEPPELIN_PASSWORD=zeppelingo  
  
RUN yum -y clean all  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y install openssh-clients  
RUN yum -y install openssl  
RUN yum -y install nginx  
RUN yum -y install httpd-tools  
  
RUN mkdir -p /etc/nginx/ssl  
RUN cd /etc/nginx/ssl && openssl req -nodes -new -x509 -keyout
/etc/nginx/ssl/server.key -out /etc/nginx/ssl/server.crt -subj
"/C=IT/ST=Italy/L=Bologna/O=YOOX/OU=IT Department/CN=*"  
  
EXPOSE 8080  
EXPOSE 8081  
EXPOSE 443  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD run.sh run.sh  
  
CMD bash run.sh  


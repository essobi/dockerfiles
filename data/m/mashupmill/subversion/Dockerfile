FROM ubuntu:14.04  
MAINTAINER mashupmill  
  
VOLUME ["/app", "/data"]  
EXPOSE 80  
ENV COMPATIBLE_VERSION=\  
USERNAME=admin\  
PASSWORD=admin  
  
COPY bootstrap.sh /app/  
  
WORKDIR /app  
RUN apt-get update &&\  
apt-get install -y apache2 apache2-utils subversion libapache2-svn && \  
apt-get autoremove -y && \  
apt-get clean && \  
usermod -U www-data && chsh -s /bin/bash www-data && \  
a2enmod rewrite cgid headers dav_svn && \  
a2dissite 000-default  
  
COPY dav_svn.conf /etc/apache2/mods-available/dav_svn.conf  
  
CMD /bin/bash /app/bootstrap.sh  


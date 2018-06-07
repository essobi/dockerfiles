FROM ubuntu:latest  
  
MAINTAINER Joshua Brooks "josh.vdbroek@gmail.com"  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Use docker host's apt-cache-ng server  
# ADD ./apt.conf /etc/apt/apt.conf  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget unzip python-software-properties xmlstarlet  
  
# Use cached key  
ADD gpg.asc /gpg.asc  
RUN cat /gpg.asc | apt-key add - && rm /gpg.asc  
  
# OR get key from server  
# RUN wget -O- http://debian.koha-community.org/koha/gpg.asc | apt-key add -  
RUN echo deb http://debian.koha-community.org/koha stable main | tee
/etc/apt/sources.list.d/koha.list  
  
RUN apt-get update  
RUN apt-get install -y apache2  
RUN sudo a2dismod mpm_event && sudo a2enmod mpm_prefork  
RUN apt-get install -y -f apache2-mpm-itk && apt-get install -f  
RUN apt-get install -y koha-common && \  
apt-get install -y -f  
RUN apt-get install -y mysql-server  
RUN apt-get clean  
  
RUN service mysql start && \  
'/usr/bin/mysqladmin' -u root password 'secret' && \  
mysql -uroot -psecret -e \  
"GRANT ALL PRIVILEGES ON *.* TO 'docker'@'%';\  
GRANT ALL ON *.* TO 'docker'@'%';\  
GRANT GRANT OPTION ON *.* TO docker@'%';\  
FLUSH PRIVILEGES;"  
RUN sed -i -e's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf  
  
RUN a2enmod rewrite &&\  
a2enmod cgi  
  
EXPOSE 80 8080  
CMD ["sudo", "/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  


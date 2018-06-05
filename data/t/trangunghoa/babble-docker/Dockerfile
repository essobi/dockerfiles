FROM ubuntu:trusty  
MAINTAINER Trang Lee <trangunghoa@gmail.com>  
  
#Install base packages  
RUN apt-get -y update  
RUN apt-get install -y openjdk-7-jre-headless  
RUN apt-get install -y tomcat7 tomcat7-admin apache2 libapache2-mod-jk  
RUN apt-get purge -y openjdk-6-jre-headless icedtea-6-jre-cacao openjdk-6-jre-
lib icedtea-6-jre-jamvm  
RUN apt-get install -y supervisor  
RUN apt-get install -y wget  
RUN apt-get install -y git  
  
# install railo  
RUN wget
http://www.getrailo.org/railo/remote/download42/4.2.1.000/tomcat/linux/railo-4.2.1.000-pl2-linux-x64-installer.run  
  
RUN chmod -R 744 railo-4.2.1.000-pl2-linux-x64-installer.run  
RUN ./railo-4.2.1.000-pl2-linux-x64-installer.run --mode unattended
--railopass 123456  
  
# remove railo setup  
RUN rm -rf railo-4.2.1.000-pl2-linux-x64-installer.run  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# start service  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# EXPOSE <port>  
EXPOSE 80 8888  
# Supervisord configuration  
#RUN mkdir /var/log/supervisor  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  


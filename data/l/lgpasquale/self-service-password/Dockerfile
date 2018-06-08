FROM debian:stable  
  
MAINTAINER Luca Pasquale  
  
RUN apt-get update && apt-get -y install wget  
RUN wget http://ltb-project.org/archives/self-service-password_1.1-1_all.deb  
RUN apt-get -y install apache2 php php-ldap php-mcrypt  
RUN dpkg -i self-service-password_1.1-1_all.deb  
  
RUN a2dissite 000-default  
RUN a2ensite self-service-password  
  
RUN apt-get install -y php-mbstring php-xml  
  
ADD ./init.sh /init.sh  
RUN chmod +x /init.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/init.sh"]  


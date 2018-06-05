FROM ubuntu:latest  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | \  
debconf-set-selections  
RUN apt-get -y update && apt-get -y install php5 php5-gd php5-mysql \  
libsolr-java zend-framework libzend-framework-php zend-framework-bin \  
libzend-framework-zendx-php php5-apcu curl imagemagick \  
libapache2-mod-php5 apache2 git mysql-client  
  
RUN git clone \--recursive --depth=1 \  
https://github.com/findsorguk/findsorguk /var/www/findsorguk  
ADD config/ /var/www/findsorguk/app/config  
  
ADD patches/ /  
ADD setup.sh /root/  
RUN /root/setup.sh && rm /root/setup.sh  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  


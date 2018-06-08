FROM bgarel/php7  
MAINTAINER Benjamin GAREL <bgarel@hotmail.com>  
  
RUN apt-get update && apt-get -y install freetds-common tdsodbc php7.0-sybase
libsybdb5 && rm -rf /var/lib/apt/lists/*  
  
COPY ./freetds.conf /etc/freetds/  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]


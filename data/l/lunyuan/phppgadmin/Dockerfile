FROM debian:jessie  
  
MAINTAINER Lun-Yuan Lee <lunyuanlee@gmail.com>  
  
ENV PG_MAJOR 9.4  
ENV TIMEZONE "Asia/Taipei"  
# Set the time zone  
RUN echo $TIMEZONE > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
RUN apt-get update  
  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get install -y wget  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get purge -y wget  
  
#RUN apt-get update  
# Install postgresql client  
RUN apt-get install -y postgresql-client-$PG_MAJOR  
  
# Install Apache  
RUN apt-get install -y apache2  
  
# Install php  
RUN apt-get install -y php5 libapache2-mod-php5 php5-mcrypt  
  
# Install phppgadmin  
RUN apt-get install -y phppgadmin  
  
RUN sed -i "s/Require local/#Require local \nRequire all granted/g"
/etc/apache2/conf-enabled/phppgadmin.conf  
RUN sed -i "s/\$conf\\['extra_login_security'\\] =
true;/\$conf\\['extra_login_security'\\] = false;/g"
/etc/phppgadmin/config.inc.php  
RUN sed -i "s/\$conf\\['servers'\\]\\[0\\]\\['host'\\] =
'localhost';/\$conf\\['servers'\\]\\[0\\]\\['host'\\] = 'db';/g"
/etc/phppgadmin/config.inc.php  
  
# Modify php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Taipei/g"
/etc/php5/apache2/php.ini  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  


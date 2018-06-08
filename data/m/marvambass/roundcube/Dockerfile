FROM marvambass/nginx-ssl-php  
MAINTAINER MarvAmBass  
  
ENV DH_SIZE 1024  
RUN apt-get update; apt-get install -y \  
wget \  
php5-intl \  
php5-mcrypt \  
php5-mysql \  
mysql-client  
  
# enable php5 mcrypt  
RUN php5enmod mcrypt  
  
# install roundcube  
RUN wget "http://sourceforge.net/projects/roundcubemail/files/latest/download"
-O roundcubemail.tar.gz && \  
tar xvf roundcubemail.tar.gz -C / && \  
rm roundcubemail.tar.gz; \  
mv /roundcube* /roundcube  
  
# fix rights  
RUN chmod a+rw /roundcube/temp/; \  
chmod a+rw /roundcube/logs/  
  
# add config  
ADD config.inc.php /roundcube/config/config.inc.php  
  
# install nginx roundcube config  
ADD nginx-roundcube.conf /etc/nginx/conf.d/nginx-roundcube.conf  
  
# add startup.sh  
ADD startup-roundcube.sh /opt/startup-roundcube.sh  
RUN chmod a+x /opt/startup-roundcube.sh  
  
# add '/opt/startup-roundcube.sh' to entrypoint.sh  
RUN sed -i 's/# exec CMD/# exec CMD\n\/opt\/startup-roundcube.sh/g'
/opt/entrypoint.sh  


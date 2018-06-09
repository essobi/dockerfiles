# Dockerfile for moodle instance. more dockerish version of
https://github.com/sergiogomez/docker-moodle  
FROM ubuntu:14.04  
MAINTAINER tokiwa  
  
VOLUME ["/var/moodledata"]  
EXPOSE 80 443  
COPY moodle-config.php /var/www/html/config.php  
  
# Keep upstart from complaining  
# RUN dpkg-divert --local --rename --add /sbin/initctl  
# RUN ln -sf /bin/true /sbin/initctl  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Database info  
#ENV MYSQL_HOST 127.0.0.1  
#ENV MYSQL_USER moodle  
#ENV MYSQL_PASSWORD moodle  
#ENV MYSQL_DB moodle  
ENV MOODLE_URL https://sample.com/moodle  
ENV MOODLE_BRANCH latest  
ENV MOODLE_VER `-b `+MOODLE_BRANCH  
  
  
# ADD http://downloads.sourceforge.net/project/moodle/Moodle/stable27/moodle-
latest-27.tgz /tmp/moodle-latest-27.tgz  
ADD ./foreground.sh /etc/apache2/foreground.sh  
  
RUN apt-get update && \  
apt-get -y install mysql-client pwgen python-setuptools curl git unzip apache2
php5 \  
php5-gd libapache2-mod-php5 postfix wget supervisor php5-pgsql curl libcurl3 \  
libcurl3-dev php5-curl php5-xmlrpc php5-intl php5-mysql git-core && \  
cd /tmp && \  
git clone git://git.moodle.org/moodle.git --depth=1 && \  
mv /tmp/moodle/* /var/www/html/ && \  
rm /var/www/html/index.html && \  
chown -R www-data:www-data /var/www/html && \  
chmod +x /etc/apache2/foreground.sh  
  
# Enable SSL, moodle requires it  
RUN a2enmod ssl && a2ensite default-ssl # if using proxy, don't need actually
secure connection  
  
CMD ["/etc/apache2/foreground.sh"]  
  
#RUN easy_install supervisor  
#ADD ./start.sh /start.sh  
#  
#ADD ./supervisord.conf /etc/supervisord.conf  
# RUN chmod 755 /start.sh /etc/apache2/foreground.sh  
# EXPOSE 22 80  
# CMD ["/bin/bash", "/start.sh"]  


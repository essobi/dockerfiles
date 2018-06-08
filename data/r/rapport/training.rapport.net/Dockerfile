##  
# Being Adapted from Sergio Gómez <sergio@quaip.com>  
# plan to switch to nginx, ports and some other config  
##  
FROM ubuntu:14.04  
MAINTAINER Gary Cornelius <gary.cornelius@rapport.net>  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Basic Requirements  
RUN apt-get -y install mysql-server mysql-client pwgen python-setuptools curl
git unzip  
  
# Moodle Requirements  
RUN apt-get -y install apache2 php5 php5-gd libapache2-mod-php5 postfix wget
supervisor php5-pgsql vim curl libcurl3 libcurl3-dev php5-curl php5-xmlrpc
php5-intl php5-mysql  
  
# SSH  
RUN apt-get -y install openssh-server  
RUN mkdir -p /var/run/sshd  
  
# mysql config  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
RUN easy_install supervisor  
ADD ./start.sh /start.sh  
ADD ./foreground.sh /etc/apache2/foreground.sh  
ADD ./supervisord.conf /etc/supervisord.conf  
  
ADD http://downloads.sourceforge.net/project/moodle/Moodle/stable27/moodle-
latest-27.tgz /var/www/moodle-latest-27.tgz  
RUN cd /var/www; tar zxvf moodle-latest-27.tgz; mv /var/www/moodle
/var/www/html  
RUN chown -R www-data:www-data /var/www/html/moodle  
RUN mkdir /var/moodledata  
RUN chown -R www-data:www-data /var/moodledata; chmod 777 /var/moodledata  
RUN chmod 755 /start.sh /etc/apache2/foreground.sh  
  
# Changing the port 8888 and will proxy through to this from nginx  
ADD config/ports.conf /etc/apache2/ports.conf  
  
# Add splash login for demo  
ADD config/index.html /var/www/html/index.html  
  
# I have moved changing apache conf port to the start.sh as that is where the
config is created  
# In /var/www/html/moodle/config.php replace "'$CFG->wwwroot =
'http://localhost/moodle';" for "'$CFG->wwwroot =
'http://localhost:8888/html/moodle';" using non-default % delimiter for url  
# sed -i 's%localhost\/moodle%localhost:8888\/moodle%g'
/var/www/html/moodle/config.php  
# Note url can be change in db fields with tool
http://localhost:8888/html/moodle/admin/tool/replace/index.php  
EXPOSE 22 80  
CMD ["/bin/bash", "/start.sh"]  
  


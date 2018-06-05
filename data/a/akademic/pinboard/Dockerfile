FROM debian:wheezy  
MAINTAINER Akademic <public@akademic.name>  
  
RUN apt-get update  
  
RUN echo 'Europe/Moscow' > /etc/timezone  
RUN DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive dpkg-
reconfigure tzdata  
  
#basic install  
RUN apt-get install -y wget mysql-server-5.5 make git  
  
RUN service mysql start  
  
#php install  
RUN apt-get install -y nginx php5-fpm php5-mysqlnd php5-cli php5-curl php5-dev  
  
#pinba install  
RUN echo 'deb http://packages.dotdeb.org wheezy all' >> /etc/apt/sources.list  
RUN wget http://www.dotdeb.org/dotdeb.gpg -O - | apt-key add -  
  
RUN apt-get update  
  
COPY ./pinba_1.1.0-1_amd64.deb /tmp/pinba_1.1.0-1_amd64.deb  
  
RUN apt-get install -y cron php5-pinba php5-apc libevent-2.0-5 libjudydebian1  
RUN dpkg -i /tmp/pinba_1.1.0-1_amd64.deb  
  
RUN wget
https://raw.githubusercontent.com/tony2001/pinba_engine/devel/default_tables.sql
-O /tmp/pinba_default_tables.sql  
RUN service mysql start && mysql -e "INSTALL PLUGIN pinba SONAME
'libpinba_engine.so';" mysql -e 'CREATE DATABASE pinba;' && mysql -D pinba <
/tmp/pinba_default_tables.sql  
  
RUN sed -i -e 's/;date.timezone =/date.timezone = Europe\/Moscow/'
/etc/php5/cli/php.ini  
RUN sed -i -e 's/;date.timezone =/date.timezone = Europe\/Moscow/'
/etc/php5/fpm/php.ini  
  
RUN git clone git://github.com/intaro/pinboard.git /opt/pinboard  
  
RUN cd /opt/pinboard && git fetch && git checkout tags  
  
RUN cd /opt/pinboard && php -r
"readfile('https://getcomposer.org/installer');" | php  
  
RUN cd /opt/pinboard && php ./composer.phar install  
  
RUN cp /opt/pinboard/config/parameters.yml.dist
/opt/pinboard/config/parameters.yml  
  
RUN sed -i 's/user: user/user: root/' /opt/pinboard/config/parameters.yml  
RUN sed -i 's/pass: password/pass: /' /opt/pinboard/config/parameters.yml  
  
RUN service mysql start && /opt/pinboard/console migrations:migrate  
RUN /opt/pinboard/console register-crontab  
  
ADD ./fpm/www.conf /etc/php5/fpm/pool.d/www.conf  
ADD ./nginx/default /etc/nginx/sites-enabled/default  
ADD ./run.sh /opt/run.sh  
  
EXPOSE 80  
EXPOSE 30002/udp  
  
CMD /opt/run.sh  


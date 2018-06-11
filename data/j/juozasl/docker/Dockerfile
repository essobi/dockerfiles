# Ubuntu 18.04, Nginx, PHP7.2, PHP7.2-cli, MongoDB 3.6, php-mongodb, snmpd,
cron support.  
FROM ubuntu:18.04  
#ENV DEBIAN_FRONTEND noninteractive  
# ++ Supervisor install  
RUN apt update && apt install -y supervisor  
COPY supervisor/* /etc/supervisor/conf.d/  
  
# ++ Mongodb install  
RUN apt update && apt install -my wget gnupg  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5  
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.6 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.6.list  
RUN apt update && apt install -y mongodb-org  
RUN sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf  
RUN sed -i 's/#security:/security:\n authorization: "enabled"/'
/etc/mongod.conf  
  
VOLUME /var/log/mongodb  
VOLUME /var/lib/mongodb  
EXPOSE 27017  
ADD set_mongo_auth.sh /set_mongo_auth.sh  
  
# ++ www server install  
RUN apt update && apt install -y nginx php-fpm php-cli php-gd php-zip php-
xmlrpc php-xml php-curl php-intl php-mbstring php-mongodb curl python-xlrd  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
# ++ config  
RUN sed -i 's/;cgi.fix_pathinfo/cgi.fix_pathinfo/' /etc/php/7.2/fpm/php.ini  
RUN sed -i 's/max_execution_time = 30/max_execution_time = 0/'
/etc/php/7.2/cli/php.ini  
COPY default_yii2 /etc/nginx/sites-available/default_yii2  
COPY default_laravel /etc/nginx/sites-available/default_laravel  
  
# ++ volumes  
VOLUME /var/www/app/  
VOLUME /var/www/log/  
  
# ++ ports  
EXPOSE 80  
# ++ snmpd install  
RUN apt update && apt install -y snmpd  
RUN echo "rocommunity public 127.0.0.1" > /etc/snmp/snmpd.conf  
RUN sed -i 's/snmpd.pid/snmpd.pid -c \/etc\/snmp\/snmpd.conf/'
/etc/default/snmpd  
  
ADD files/checksupervisor.sh /usr/local/bin/checksupervisor.sh  
  
VOLUME /etc/snmp/  
EXPOSE 161/udp  
  
# ++ crons support  
RUN apt update && apt install -y cron run-one  
RUN touch /etc/cron.d/app  
RUN chmod 0644 /etc/cron.d/app  
  
VOLUME /etc/cron.d/  
  
WORKDIR /var/www/app  
  
# ++ run all necessary daemons  
ADD run.sh /run.sh  
ENTRYPOINT ["/run.sh"]  
  


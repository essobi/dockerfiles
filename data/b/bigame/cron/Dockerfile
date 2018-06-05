FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6\  
&&echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list  
  
RUN apt-get update;  
RUN apt-get install -y --no-install-recommends php-cli php-mcrypt php-xdebug
php-amqp php-mongodb php-redis php-mbstring php-gd php-mysql php-curl php-
igbinary php-xml php-apcu curl\  
mysql-client-5.7\  
mongodb-org-tools mongodb-org-shell\  
redis-tools\  
cron\  
vim\  
bash-completion\  
openssh-client\  
ca-certificates\  
rsync\  
&&rm -rf /var/lib/apt/lists/*  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh  
  
RUN cp /usr/share/zoneinfo/PRC /etc/localtime  
  
VOLUME "/etc/cron.d"  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["cron", "start","-f"]


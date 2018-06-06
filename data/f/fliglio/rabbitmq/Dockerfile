FROM ubuntu:14.04  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y \  
php5-cli php5-fpm php5-mysql php5-pgsql php5-sqlite php5-curl \  
php5-gd php5-mcrypt php5-intl php5-imap php5-tidy php5-memcache  
RUN apt-get install -y \  
nginx \  
memcached \  
mysql-server mysql-client \  
supervisor  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/cli/php.ini  
  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /var/www  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
  
ADD nginx-site /etc/nginx/sites-available/default  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stdout /var/log/nginx/error.log  
  
RUN /usr/sbin/mysqld & \  
sleep 10s &&\  
echo "GRANT ALL ON *.* TO admin@'%' IDENTIFIED BY 'changeme' WITH GRANT
OPTION; FLUSH PRIVILEGES" | mysql  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# consul  
RUN apt-get install -y unzip  
ADD https://releases.hashicorp.com/consul/0.6.0/consul_0.6.0_linux_amd64.zip
/tmp/consul.zip  
RUN cd /tmp && unzip consul.zip && chmod 755 consul && mv consul /bin/consul
&& rm consul.zip  
  
ADD https://releases.hashicorp.com/consul/0.6.0/consul_0.6.0_web_ui.zip
/tmp/webui.zip  
RUN mkdir /ui && cd /ui && unzip /tmp/webui.zip && rm /tmp/webui.zip  
  
# rabbitmq  
RUN apt-get install -y rabbitmq-server  
RUN rabbitmq-plugins enable rabbitmq_management  
  
# chinchilla  
RUN apt-get install -y curl  
ADD https://drone.io/github.com/benschw/chinchilla/files/chinchilla.gz
/tmp/chinchilla.gz  
RUN cd /tmp && gunzip chinchilla.gz && chmod 755 chinchilla && mv chinchilla
/bin/chinchilla  
  
ADD configure-chinchilla.sh /tmp/configure-chinchilla.sh  
  
# configure  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD phinx.php /etc/phinx.php  
ADD migrate.sh /usr/local/bin/migrate.sh  
ADD run.sh /usr/local/bin/run.sh  
  
EXPOSE 80  
EXPOSE 3306  
EXPOSE 8500  
EXPOSE 15672  
CMD ["/usr/local/bin/run.sh"]  
  


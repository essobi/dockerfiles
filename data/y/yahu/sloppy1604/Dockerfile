FROM ubuntu:16.04  
MAINTAINER Thomas Van<thomas@forixwebdesign.com>  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
RUN mkdir /var/run/sshd  
RUN mkdir /run/php  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Basic Requirements  
RUN apt-get -y install curl sudo python-setuptools cron ca-certificates zip
openssh-server openssl wget vim  
# RUN apt-get -y install mysql-server mysql-client nginx php-fpm php-mysql  
RUN apt-get -y install nginx php-fpm  
  
# Wordpress Requirements  
# RUN apt-get -y install php-xml php-mbstring php-bcmath php-zip php-pdo-mysql
php-curl php-gd php-intl php-pear php-imagick php-imap php-mcrypt php-memcache
php-apcu php-pspell php-recode php-tidy php-xmlrpc  
RUN apt-get -y install php-mbstring php-zip php-curl php-gd php-mcrypt  
  
# mysql config  
# RUN sed -i -e"s/^bind-
address\s*=\s*127.0.0.1/explicit_defaults_for_timestamp = true\nbind-address =
0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf  
# nginx config  
RUN sed -i -e"s/user\s*www-data;/user ubuntu www-data;/" /etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# php-fpm config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i -e "s/user\s*=\s*www-data/user = ubuntu/g"
/etc/php/7.0/fpm/pool.d/www.conf  
# replace # by ; RUN find /etc/php/7.0/mods-available/tmp -name "*.ini" -exec
sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;  
# nginx site conf  
ADD ./nginx-site.conf /etc/nginx/sites-available/default  
  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Add system user for ubuntu  
RUN useradd -m -d /home/ubuntu -p $(openssl passwd -1
'Bmi3d)g^rK?bHFpdRj9(X4K-') -G root -s /bin/bash ubuntu \  
&& usermod -a -G www-data ubuntu \  
&& usermod -a -G sudo ubuntu \  
&& mkdir -p /home/ubuntu/wwwroot  
  
ADD wwwroot/ /home/ubuntu/wwwroot  
  
RUN chown -R ubuntu:www-data /home/ubuntu/wwwroot \  
&& chmod -R 775 /home/ubuntu/wwwroot  
  
# add our cron stub  
# ADD crontab /etc/cron.d/ubphp  
# RUN chmod 0644 /etc/cron.d/ubphp  
ADD crontab /var/spool/cron/crontabs/ubuntu  
RUN chmod 0600 /var/spool/cron/crontabs/ubuntu  
  
#ssh key files  
ADD authorized_keys /authorized_keys  
RUN mkdir -p /root/.ssh && \  
mkdir -p /home/ubuntu/.ssh && \  
chmod 700 /root/.ssh && \  
chmod 700 /home/ubuntu/.ssh && \  
cp /authorized_keys /root/.ssh/. && \  
cp /authorized_keys /home/ubuntu/.ssh && \  
chmod 600 /root/.ssh/* && \  
chmod 600 /home/ubuntu/.ssh/* && \  
chown -Rf root:root /root/.ssh && \  
chown -Rf ubuntu:ubuntu /home/ubuntu/.ssh  
  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/'
/etc/ssh/sshd_config  
  
# ubuntu Initialization and Startup Script  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
RUN apt-get -y autoremove && \  
apt-get autoclean  
  
#NETWORK PORTS  
# EXPOSE 9011  
EXPOSE 80  
EXPOSE 22  
# volume for mysql database and wordpress install  
# VOLUME ["/var/lib/mysql", "/home/ubuntu/wwwroot", "/var/run/sshd"]  
CMD ["/bin/bash", "/start.sh"]  


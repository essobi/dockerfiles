# homestead  
# todo: # install prestissimo composer并发安装利器  
#  
# VERSION 0.0.1  
FROM ubuntu:14.04  
MAINTAINER x-bird <x-bird@qiubs.com>  
  
# set the locale  
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale  
RUN locale-gen en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# PASSWORD  
ENV PASSWORD `mkpasswd 123123`  
  
  
  
  
# Set The Timezone  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:123123' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# install supervisor  
RUN apt-get update && \  
apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add A Few PPAs To Stay Current  
RUN apt-get install -y --force-yes software-properties-common  
  
RUN apt-add-repository ppa:fkrull/deadsnakes-python2.7 -y  
RUN apt-add-repository ppa:nginx/development -y  
RUN apt-add-repository ppa:rwky/redis -y  
RUN apt-add-repository ppa:ondrej/apache2 -y  
RUN apt-add-repository ppa:ondrej/php -y  
  
# Setup MySQL 5.7 Repositories  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 5072E1F5  
RUN echo "deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7" >>
/etc/apt/sources.list.d/mysql.list  
  
# Setup Postgres 9.4 Repositories  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/postgresql.list  
  
# Update Package Lists  
RUN apt-get update  
# Base Packages  
RUN apt-get install -y --force-yes build-essential curl fail2ban gcc git
libmcrypt4 libpcre3-dev make python2.7 python-pip supervisor ufw unattended-
upgrades unzip whois zsh  
  
# Install Python Httpie  
RUN pip install httpie  
  
# Restart SSH  
RUN ssh-keygen -A  
RUN service ssh restart  
  
RUN if [ ! -d /root/.ssh ]; then mkdir -p /root/.ssh; touch
/root/.ssh/authorized_keys; fi  
  
RUN useradd forzu  
RUN mkdir -p /home/forzu/.ssh  
RUN mkdir -p /home/forzu/.forzu  
RUN adduser forzu sudo  
  
# Setup Bash For Forzu User  
RUN chsh -s /bin/bash forzu  
RUN cp /root/.profile /home/forzu/.profile  
RUN cp /root/.bashrc /home/forzu/.bashrc  
  
# Set The Sudo Password For Forzu  
# RUN usermod --password ${PASSWORD} forzu // 这句命令会报错 ：The command '/bin/sh -c
usermod --password ${PASSWORD} forzu' returned a non-zero code: 2  
RUN ["usermod", "--password", "echo $PASSWORD", "forzu"]  
  
RUN cp /root/.ssh/authorized_keys /home/forzu/.ssh/authorized_keys  
  
# Create The Server SSH Key  
RUN ssh-keygen -f /home/forzu/.ssh/id_rsa -t rsa -N ''  
RUN git config --global user.name "x-bird"  
RUN git config --global user.email "x-bird@qiubs.com"  
  
# Add The Reconnect Script Into Forzu Directory  
RUN echo " \n\  
#!/usr/bin/env bash \n\  
\n\  
echo "# Laravel Forzu" | tee -a /home/forzu/.ssh/authorized_keys > /dev/null
\n\  
echo \$1 | tee -a /home/forzu/.ssh/authorized_keys > /dev/null \n\  
\n\  
echo "# Laravel Forzu" | tee -a /root/.ssh/authorized_keys > /dev/null \n\  
echo \$1 | tee -a /root/.ssh/authorized_keys > /dev/null \n\  
\n\  
echo "Keys Added!" \n\  
" >> /home/forzu/.forzu/reconnect  
  
# Add The Environment Variables Scripts Into Forzu Directory  
RUN echo " \n\  
<?php \n\  
\n\  
// Get the script input... \n\  
\$input = array_values(array_slice(\$_SERVER['argv'], 1)); \n\  
\n\  
// Get the path to the environment file... \n\  
\$path = getcwd().'/'.\$input[2]; \n\  
\n\  
// Write a stub file if one doesn't exist... \n\  
if ( ! file_exists(\$path)) { \n\  
file_put_contents(\$path, '<?php return '.var_export([], true).';'); \n\  
} \n\  
\n\  
// Set the new environment variable... \n\  
\$env = require \$path; \n\  
\$env[\$input[0]] = \$input[1]; \n\  
\n\  
// Write the environment file to disk... \n\  
file_put_contents(\$path, '<?php return '.var_export(\$env, true).';'); \n\  
\n\  
\n\  
" >> /home/forzu/.forzu/add-variable.php  
  
RUN echo " \n\  
<?php \n\  
\n\  
// Get the script input... \n\  
\$input = array_values(array_slice(\$_SERVER['argv'], 1)); \n\  
\n\  
// Get the path to the environment file... \n\  
\$path = getcwd().'/'.\$input[1]; \n\  
\n\  
// Write a stub file if one doesn't exist... \n\  
if ( ! file_exists(\$path)) { \n\  
file_put_contents(\$path, '<?php return '.var_export([], true).';'); \n\  
} \n\  
\n\  
// Remove the environment variable... \n\  
\$env = require \$path; \n\  
unset(\$env[\$input[0]]); \n\  
\n\  
// Write the environment file to disk... \n\  
file_put_contents(\$path, '<?php return '.var_export(\$env, true).';'); \n\  
\n\  
\n\  
" >> /home/forzu/.forzu/remove-variable.php  
  
# Setup Site Directory Permissions  
RUN chown -R forzu:forzu /home/forzu  
RUN chmod -R 755 /home/forzu  
RUN chmod 700 /home/forzu/.ssh/id_rsa  
  
# Setup Unattended Security Upgrades  
RUN echo " \n\  
Unattended-Upgrade::Allowed-Origins { \n\  
"Ubuntu trusty-security"; \n\  
}; \n\  
Unattended-Upgrade::Package-Blacklist { \n\  
// \n\  
}; \n\  
" >> /etc/apt/apt.conf.d/50unattended-upgrades  
  
RUN echo " \n\  
APT::Periodic::Update-Package-Lists "1"; \n\  
APT::Periodic::Download-Upgradeable-Packages "1"; \n\  
APT::Periodic::AutocleanInterval "7"; \n\  
APT::Periodic::Unattended-Upgrade "1"; \n\  
" >> /etc/apt/apt.conf.d/10periodic  
  
# Setup UFW Firewall # 不需要利用docker的防火墙  
# RUN ufw allow 22  
# RUN ufw allow 80  
# RUN ufw allow 443  
# RUN ufw --force enable  
# Allow FPM Restart  
RUN echo "forzu ALL=NOPASSWD: /usr/sbin/service php7.0-fpm reload" >
/etc/sudoers.d/php-fpm  
RUN echo "forzu ALL=NOPASSWD: /usr/sbin/service php5-fpm reload" >>
/etc/sudoers.d/php-fpm  
  
# Install Base PHP Packages  
RUN apt-get install -y --force-yes php7.0-cli php7.0-dev \  
php-pgsql php-sqlite3 php-gd \  
php-curl php7.0-dev \  
php-imap php-mysql php-memcached php-mcrypt  
  
# Install Composer Package Manager  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Misc. PHP CLI Configuration  
RUN sudo sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.0/cli/php.ini  
RUN sudo sed -i "s/display_errors = .*/display_errors = On/"
/etc/php/7.0/cli/php.ini  
RUN sudo sed -i "s/memory_limit = .*/memory_limit = 512M/"
/etc/php/7.0/cli/php.ini  
RUN sudo sed -i "s/;date.timezone.*/date.timezone = UTC/"
/etc/php/7.0/cli/php.ini  
  
# Configure Sessions Directory Permissions  
RUN chmod 733 /var/lib/php/sessions  
RUN chmod +t /var/lib/php/sessions  
  
# Install Nginx & PHP-FPM  
RUN apt-get install -y --force-yes nginx php7.0-fpm  
  
# Disable The Default Nginx Site  
RUN rm /etc/nginx/sites-enabled/default  
RUN rm /etc/nginx/sites-available/default  
RUN service nginx restart  
  
# Tweak Some PHP-FPM Settings  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.0/fpm/php.ini  
  
RUN sed -i "s/display_errors = .*/display_errors = On/"
/etc/php/7.0/fpm/php.ini  
  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.0/fpm/php.ini  
  
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/7.0/fpm/php.ini  
  
RUN sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.0/fpm/php.ini  
  
# Setup Session Save Path  
RUN sed -i "s/\;session.save_path = .*/session.save_path =
\"\/var\/lib\/php5\/sessions\"/" /etc/php/7.0/fpm/php.ini  
RUN sed -i "s/php5\/sessions/php\/sessions/" /etc/php/7.0/fpm/php.ini  
  
# Configure Nginx & PHP-FPM To Run As Forzu  
RUN sed -i "s/user www-data;/user forzu;/" /etc/nginx/nginx.conf  
  
RUN sed -i "s/# server_names_hash_bucket_size.*/server_names_hash_bucket_size
64;/" /etc/nginx/nginx.conf  
  
RUN sed -i "s/^user = www-data/user = forzu/" /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i "s/^group = www-data/group = forzu/"
/etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i "s/;listen\\.owner.*/listen.owner = forzu/"
/etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i "s/;listen\\.group.*/listen.group = forzu/"
/etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i "s/;listen\\.mode.*/listen.mode = 0666/"
/etc/php/7.0/fpm/pool.d/www.conf  
  
# Configure A Few More Server Things  
RUN sed -i "s/;request_terminate_timeout.*/request_terminate_timeout = 60/"
/etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i "s/worker_processes.*/worker_processes auto;/"
/etc/nginx/nginx.conf  
RUN sed -i "s/# multi_accept.*/multi_accept on;/" /etc/nginx/nginx.conf  
  
# Install A Catch All Server  
RUN echo " \n\  
server { \n\  
return 404; \n\  
} \n\  
" >> /etc/nginx/sites-available/catch-all  
  
RUN ln -s /etc/nginx/sites-available/catch-all /etc/nginx/sites-enabled/catch-
all  
  
# Restart Nginx & PHP-FPM Services  
# Restart Nginx & PHP-FPM Services  
RUN if [ ! -z "\$(ps aux | grep php-fpm | grep -v grep)" ]; then service
php5-fpm restart; service php7.0-fpm restart; fi  
  
RUN service nginx restart  
RUN service nginx reload  
  
# Add Forzu User To www-data Group  
RUN usermod -a -G www-data forzu  
RUN id forzu  
RUN groups forzu  
  
RUN curl --silent --location https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get update  
RUN sudo apt-get install -y --force-yes nodejs  
RUN npm install -g pm2  
RUN npm install -g gulp  
  
#  
# REQUIRES:  
# - server (the forzu server instance)  
# - db_password (random password for mysql user)  
#  
# Set The Automated Root Password  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN ["/bin/sh", "-c", "debconf-set-selections", "<<<", "mysql-community-server
mysql-community-server/data-dir select ''"]  
RUN ["/bin/sh", "-c", "debconf-set-selections", "<<<", "mysql-community-server
mysql-community-server/root-pass password 123123"]  
RUN ["/bin/sh", "-c", "debconf-set-selections", "<<<", "mysql-community-server
mysql-community-server/re-root-pass password 123123"]  
# RUN debconf-set-selections <<< "mysql-community-server mysql-community-
server/data-dir select ''"  
# RUN debconf-set-selections <<< "mysql-community-server mysql-community-
server/root-pass password 123123"  
# RUN debconf-set-selections <<< "mysql-community-server mysql-community-
server/re-root-pass password 123123"  
# Install MySQL  
RUN apt-get install -y mysql-server  
  
# Configure Password Expiration  
RUN echo "default_password_lifetime = 0" >> /etc/mysql/my.cnf  
  
# Configure Access Permissions For Root & Forzu Users  
RUN sed -i '/^bind-address/s/bind-address.*=.*/bind-address = */'
/etc/mysql/my.cnf  
RUN /usr/sbin/mysqld & \  
sleep 10s && \  
mysql --user="root" \--password="123123" -e "GRANT ALL ON *.* TO
root@'123.123.123.123' IDENTIFIED BY '123123';" && \  
mysql --user="root" \--password="123123" -e "GRANT ALL ON *.* TO root@'%'
IDENTIFIED BY '123123';" && \  
mysql --user="root" \--password="123123" -e "CREATE USER
'forzu'@'123.123.123.123' IDENTIFIED BY '123123';" && \  
mysql --user="root" \--password="123123" -e "GRANT ALL ON *.* TO
'forzu'@'123.123.123.123' IDENTIFIED BY '123123' WITH GRANT OPTION;" && \  
mysql --user="root" \--password="123123" -e "GRANT ALL ON *.* TO 'forzu'@'%'
IDENTIFIED BY '123123' WITH GRANT OPTION;" && \  
mysql --user="root" \--password="123123" -e "FLUSH PRIVILEGES;" && \  
mysql --user="root" \--password="123123" -e "CREATE DATABASE forzu;"  
  
#  
# REQUIRES:  
# - server (the forzu server instance)  
# - db_password (random password for database user)  
#  
# Install Postgres  
# RUN apt-get install -y --force-yes postgresql-9.4  
# # Configure Postgres For Remote Access  
# RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g"
/etc/postgresql/9.4/main/postgresql.conf  
# RUN echo "host all all 0.0.0.0/0 md5" | tee -a
/etc/postgresql/9.4/main/pg_hba.conf  
# RUN sudo -u postgres psql -c "CREATE ROLE forzu LOGIN UNENCRYPTED PASSWORD
'123123' SUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;"  
# RUN service postgresql restart  
# # Create The Initial Database If Specified  
# RUN sudo -u postgres /usr/bin/createdb --echo --owner=forzu forzu  
# Install & Configure Redis Server  
RUN apt-get install -y redis-server  
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf  
# RUN service redis-server restart  
# Install & Configure Memcached  
RUN apt-get install -y memcached  
RUN sed -i 's/-l 127.0.0.1/-l 0.0.0.0/' /etc/memcached.conf  
# RUN service memcached restart  
# Install & Configure Beanstalk  
RUN apt-get install -y --force-yes beanstalkd  
RUN sed -i "s/BEANSTALKD_LISTEN_ADDR.*/BEANSTALKD_LISTEN_ADDR=0.0.0.0/"
/etc/default/beanstalkd  
RUN sed -i "s/#START=yes/START=yes/" /etc/default/beanstalkd  
# RUN /etc/init.d/beanstalkd start  
EXPOSE 22 80 443 3306 6379  
CMD ["/usr/bin/supervisord"]  
  
# set container entrypoints  
ENTRYPOINT ["/bin/bash","-c"]  


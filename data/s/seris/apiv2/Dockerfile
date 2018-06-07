#  
# Nginx and Mongo Dockerfile  
# https://github.com/dockerfile/nginx  
# Dockerizing MongoDB: Dockerfile for building MongoDB images  
# Based on ubuntu:latest, installs MongoDB following the instructions from:  
# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/  
# Pull base image.  
FROM ubuntu:latest  
MAINTAINER seris  
  
# Install vim/vi & curl  
RUN \  
apt-get update && \  
apt-get install -y vim && \  
apt-get install -y curl  
  
# Install PHP  
RUN \  
apt-get update && \  
apt-get install -y php7.0-fpm php-mongodb  
  
# Configuring PHP processor  
RUN \  
awk '{ gsub(";cgi.fix_pathinfo=1","cgi.fix_pathinfo=0"); print}'
/etc/php/7.0/fpm/php.ini > /etc/php/7.0/fpm/php.ini_tmp && \  
mv /etc/php/7.0/fpm/php.ini_tmp /etc/php/7.0/fpm/php.ini  
  
# Install MONGODB  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
# this VOLUME ["/data/db"] will go with the VOLUME from nginx below  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
#CMD ["mongod"] -- this has been included in a startup shell script so both
mongo and nginx are started  
# Expose ports.  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  
# Install NGINX  
# removed this line as first RUN add-apt-repository -y ppa:nginx/stable && \  
RUN \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
#echo "/usr/bin/mongod &\n/usr/sbin/nginx &\n /etc/init.d/php7.0-fpm start" >
/etc/onstartup.sh  
# We will pull the nginx configuration to use PHP  
# VERY IMPORTANT: substitute the url below for the correct location of the
nginx conf file for PHP  
RUN \  
curl https://raw.githubusercontent.com/iserranoba/docker/apiv2/RESTAPI/nginx-
default-file -o /tmp/nginx-conf && \  
mv /tmp/nginx-conf /etc/nginx/sites-available/default  
  
# Create the script to startup the proceses. We will leave mongo to execute
last in order to allow the container run in deamon mode  
# echo "/etc/init.d/mongod start \n/etc/init.d/nginx start
\n/etc/init.d/php7.0-fpm start" > /etc/onstartup.sh  
RUN \  
echo "/etc/init.d/nginx start & \n/etc/init.d/php7.0-fpm start &
\n/usr/bin/mongod --smallfiles" > /etc/onstartup.sh  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html", "/data/db"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command. This should start the mongod and nginx deamons  
CMD ["/bin/bash", "/etc/onstartup.sh"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
# Now that we have all the necessary stuff in the container, we need to modify
files  
# from: https://www.digitalocean.com/community/tutorials/how-to-install-linux-
nginx-mysql-php-lemp-stack-in-ubuntu-16-04  


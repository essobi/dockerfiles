FROM debian:jessie-slim  
  
ENV MYSQL_ROOT_PASSWORD Tigrou007 \  
MYSQL_DATABASE_HOST wordpressdb \  
WP_MYSQL_DATABASE vitrine_wordpress \  
MYSQL_USER db_user_project_name \  
MYSQL_PASSWORD db_user_project_password \  
PROJECT_DOMAIN projectdomain \  
PROJECT_NAME_WITH_SPACES projectnamewithspaces \  
WEBMASTER_LOGIN=webmaster \  
WEBMASTER_PASSWORD=Tigrou007  
  
RUN apt-get update && \  
apt-get install debconf-utils && \  
export DEBIAN_FRONTEND="noninteractive" && \  
apt-get -y install --no-install-recommends wget curl ca-certificates apache2
&& \  
echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list
&& \  
wget -O- https://www.dotdeb.org/dotdeb.gpg | apt-key add - apt update && \  
apt-get update && \  
apt-get -y install --no-install-recommends php7.0 libapache2-mod-php7.0
php7.0-mysql php7.0-curl php7.0-json php7.0-gd php7.0-mcrypt php7.0-msgpack
php7.0-intl php7.0-gmp php7.0-geoip php7.0-mbstring php7.0-xml php7.0-zip  
  
RUN curl -O https://wordpress.org/wordpress-4.9.6.tar.gz && \  
tar xzvf wordpress-4.9.6.tar.gz && \  
mkdir /var/www/wordpress && \  
mkdir /var/www/wordpress/public_html && \  
mv -v /wordpress/* /var/www/wordpress/public_html && \  
touch /var/www/wordpress/public_html/.htaccess && \  
chmod 660 /var/www/wordpress/public_html/.htaccess  
  
ADD wordpress.sh /wordpress.sh  
RUN chmod +x /wordpress.sh  
ADD wordpress.conf /etc/apache2/sites-available/wordpress.conf  
ADD wp-config.php /var/www/wordpress/public_html/wp-config.php  
ADD init-users.php /init-users.php  
RUN chmod +x /init-users.php  
  
EXPOSE 80/tcp  
EXPOSE 443/tcp  
  
ENTRYPOINT ["/wordpress.sh"]  


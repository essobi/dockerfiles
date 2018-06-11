FROM php:5.6-fpm  
  
MAINTAINER Andreas Åkre Solberg <andreas@solweb.no>  
  
# ------------------  
# PHP & EXTENSIONS  
# ------------------  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev pwgen python-setuptools curl
git unzip wget git nginx nano \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache zip mbstring pdo_mysql  
  
# ------------------  
# HOME/WORKING DIR  
# ------------------  
RUN mkdir /app  
WORKDIR /app  
  
# ------------------  
# SUPERVISOR  
# ------------------  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
  
# ------------------  
# COMPOSER  
# ------------------  
RUN bash -c "wget http://getcomposer.org/composer.phar && mv composer.phar
/usr/local/bin/composer"  
RUN chmod a+x /usr/local/bin/composer  
  
# ------------------  
# FLARUM  
# ------------------  
# RUN /usr/local/bin/composer create-project flarum/flarum . v0.1.0-beta.6
--stability=beta  
RUN /usr/local/bin/composer create-project flarum/flarum . v0.1.0-beta.6
--stability=beta  
RUN chmod -R a+rX .  
  
# Add an 'ENV-version' of Flarum's config file (in case we do not want a new
Flarum install)  
COPY etc/flarum/config.php config.php_  
  
#RUN cp -a vendor/flarum/core/assets/fonts/ assets/fonts/  
RUN cp -a vendor/components/font-awesome/fonts/ assets/fonts/  
  
# Dataporten extension  
RUN composer require uninett/flarum-ext-auth-dataporten  
  
# Temporary fix for Zend-framework  
RUN composer require zendframework/zend-stratigility:1.2.*  
  
# Norwegian translation extension  
RUN composer require pladask/flarum-ext-norwegian-bokmal  
  
# Set permissions  
RUN chmod 775 /app  
RUN chmod -R 775 /app/storage  
RUN chmod -R 775 /app/assets  
RUN chown -R root:www-data /app  
  
# ------------------  
# NGINX  
# ------------------  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
COPY etc/supervisord.conf /etc/supervisord.conf  
COPY etc/nginx-site.conf /etc/nginx/sites-available/default  
  
# ------------------  
# INSTALLING FLARUM-DB (Has failsafe for when database already exists)  
# ------------------  
COPY etc/config.yaml /config.yaml  
  
# ------------------  
# SERVICES  
# ------------------  
COPY etc/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# ------------------  
# FLARUM-LOOKS  
# ------------------  
RUN echo "#other_sites_container{ background: white; /* width: 100%; */
margin: 20px; position: fixed; padding: 10px; bottom: 0px; right: 0px; border-
radius: 8px; z-index: 99999; border: 0.5px solid black;}#other_sites_container
a, #other_sites_container a:focus, #other_sites_container a:visited{ color:
red;}#other_sites_container a:hover{ color: coral;}" >>
/app/vendor/flarum/core/less/forum/app.less  
RUN echo "echo \"<div id='other_sites_container'><a
href='https://chat.uninett.no'>Chat</a> | <span id='active_site'>Flarum</span>
| <a href='https://samskrive.uninett.no'>Samskrive</a></div>\";" >>
/app/index.php  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  


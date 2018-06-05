FROM debian:jessie  
MAINTAINER Sam <s.j.finnigan@ncl.ac.uk>  
  
# This dockerfile is suitable for installing Wordpress  
# installation. The script will also look for /data volume  
# in anticipation of an existing wordpress install. If it's  
# found, then it will analyse it's contents and will  
# link assets like this:  
#  
# data/wp-content folder symlinked  
# data/.htaccess symlinked  
# data/init.sh script initialized  
# Install a web stack  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \  
unzip zip \  
mysql-client \  
nginx-extras \  
php5-fpm \  
php5-mysql \  
php5-ldap \  
php5-gd \  
libssh2-php \  
php5-curl \  
php-pear \  
postfix && rm -rf /var/lib/apt/lists/*  
  
# PHP security & Allow variables from environment  
RUN sed -i "s/cgi.fix_pathinfo.\\+/cgi.fix_pathinfo = 0/"
/etc/php5/fpm/php.ini  
RUN echo "clear_env = no" >> /etc/php5/fpm/php-fpm.conf  
  
# Increase PHP upload size  
RUN sed -i 's/upload_max_filesize.\\+/upload_max_filesize = 200M/'
/etc/php5/fpm/php.ini  
RUN sed -i 's/post_max_size.\\+/post_max_size = 200M/' /etc/php5/fpm/php.ini  
  
# Limit workers to keep memory use low (remove for high volume apps)  
RUN sed -i 's/worker_processes.\\+/worker_processes 1;/' /etc/nginx/nginx.conf  
RUN sed -i 's/worker_connections.\\+/worker_connections 1024;/'
/etc/nginx/nginx.conf  
RUN sed -i 's/^pm.max_children =.\\+/pm.max_children = 3/'
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i 's/^pm.start_servers =.\\+/pm.start_servers = 1/'
/etc/php5/fpm/pool.d/www.conf  
  
# Set up relayhost for postfix / PHP mail() function  
RUN sed -i 's/relayhost =/relayhost = smtp.ncl.ac.uk/' /etc/postfix/main.cf  
RUN sed -ri '/^smtp(d)?_(.+)?tls.+/d' /etc/postfix/main.cf  
  
# Make directory for web files  
RUN mkdir -p /var/www/html  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
  
# Collect nginx logs  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Install vanilla wordpress  
ADD https://wordpress.org/latest.tar.gz /wordpress.tar.gz  
RUN tar xzf /wordpress.tar.gz  
RUN cp -aR /wordpress/* /app  
RUN chown -R www-data:www-data /app  
  
# Use our default config  
ADD wp-config.php /app/wp-config.php  
ADD sso-plugin.php /app/wp-content/plugins/sso.php  
  
# Copy CHECKS  
COPY CHECKS /app/CHECKS  
  
# Declare a persistent data directory  
VOLUME /data  
  
# Initialize custom config from volume  
ADD volume-init.sh /volume-init.sh  
RUN chmod 755 /volume-init.sh  
  
# Configure and start nginx  
ADD nginx-default /etc/nginx/sites-available/default  
RUN echo "fastcgi_param AUTH_TYPE $http_auth_type if_not_empty;" >>
/etc/nginx/fastcgi_params \  
&& echo "fastcgi_param REMOTE_USER $http_remote_user if_not_empty;" >>
/etc/nginx/fastcgi_params \  
&& echo "fastcgi_param SSO_KNOWNAS $http_sso_knownas if_not_empty;" >>
/etc/nginx/fastcgi_params \  
&& echo "fastcgi_param SSO_SN $http_sso_sn if_not_empty;" >>
/etc/nginx/fastcgi_params \  
&& echo "fastcgi_param SSO_GROUPS $http_sso_groups if_not_empty;" >>
/etc/nginx/fastcgi_params \  
&& echo "fastcgi_param SSO_MAIL $http_sso_mail if_not_empty;" >>
/etc/nginx/fastcgi_params \  
&& echo "fastcgi_param SSO_GIVENNAME $http_sso_givenname if_not_empty;" >>
/etc/nginx/fastcgi_params  
ADD run.sh /run.sh  
  
# Declare volumes to persist  
VOLUME /data  
  
EXPOSE 80  
WORKDIR /app  
CMD /run.sh  


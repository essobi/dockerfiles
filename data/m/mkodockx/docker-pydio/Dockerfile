FROM dockerfile/supervisor  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
ENV PYDIO_VERSION 6.0.3  
ENV DB_NAME pydiodb  
ENV DB_USER pydiomgr  
ENV DB_PASS wH00pDaRoot  
  
#
------------------------------------------------------------------------------  
# Install Base  
RUN apt-get update  
RUN apt-get install -yq wget nano unzip nginx fontconfig-config fonts-dejavu-
core \  
php5-fpm php5-common php5-json php5-cli php5-common php5-mysql sendmail \  
php5-gd php5-json php5-mcrypt php5-readline psmisc ssl-cert \  
ufw php-pear libgd-tools libmcrypt-dev mcrypt mysql-server mysql-client  
  
#
------------------------------------------------------------------------------  
# Configure mysql  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN service mysql start && \  
mysql -uroot -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};" && \  
mysql -uroot -e "CREATE USER '${DB_USER}'@'localhost' IDENTIFIED BY
'${DB_PASS}';" && \  
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO '${DB_USER}'@'localhost' WITH
GRANT OPTION;" && \  
mysql -uroot -e "FLUSH PRIVILEGES;"  
  
#
------------------------------------------------------------------------------  
# Configure php-fpm  
RUN sed -i -e "s/output_buffering\s*=\s*4096/output_buffering = Off/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 1G/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size=1G/g"
/etc/php5/fpm/php.ini  
  
RUN sed -i -e "s/pm.max_children\s*=\s*5/pm.max_children = 10/g"
/etc/php5/fpm/pool.d/www.conf  
  
RUN php5enmod mcrypt  
  
#
------------------------------------------------------------------------------  
# Configure nginx  
RUN mkdir /var/www  
RUN chown www-data:www-data /var/www  
RUN rm /etc/nginx/sites-enabled/*  
RUN rm /etc/nginx/sites-available/*  
# RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 20/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout
20;\n\tclient_max_body_size 1G/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD conf/drop.conf /etc/nginx/  
ADD conf/php.conf /etc/nginx/  
ADD conf/pydio /etc/nginx/sites-enabled/  
  
#
------------------------------------------------------------------------------  
# Configure services  
RUN update-rc.d nginx defaults  
RUN update-rc.d php5-fpm defaults  
RUN update-rc.d mysql defaults  
  
#
------------------------------------------------------------------------------  
# Install Pydio  
WORKDIR /var/www  
# RUN wget http://downloads.sourceforge.net/project/ajaxplorer/pydio/dev-
channel/5.3.2/pydio-core-5.3.2.zip  
RUN wget "http://sourceforge.net/projects/ajaxplorer/files/pydio/stable-
channel/${PYDIO_VERSION}/pydio-core-${PYDIO_VERSION}.zip"  
RUN unzip pydio-core-${PYDIO_VERSION}.zip && mv /var/www/pydio-
core-${PYDIO_VERSION} /var/www/pydio && rm -rf /var/www/pydio-core-*  
RUN chown -R www-data:www-data /var/www/pydio  
RUN chown -R www-data:www-data /tmp  
RUN chmod -R 770 /var/www/pydio  
RUN chmod 777 /var/www/pydio/data/files/  
RUN chmod 777 /var/www/pydio/data/personal/  
  
WORKDIR /  
RUN ln -s /var/www/pydio/data pydio-data  
#
------------------------------------------------------------------------------  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
# two additional ports to use with WS server  
EXPOSE 18081  
EXPOSE 10801  
#
------------------------------------------------------------------------------  
# Expose volumes  
VOLUME /pydio-data/files  
VOLUME /pydio-data/personal  
  
#
------------------------------------------------------------------------------  
# Add supervisord conf  
ADD conf/startup.conf /etc/supervisor/conf.d/  
  
# Start supervisor, define default command.  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]


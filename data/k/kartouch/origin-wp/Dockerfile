FROM centos:centos7  
  
ENV NGINX_HOME /var/www/wordpress  
  
# Update image os/ Install nginx php + php libs / clear yum data  
RUN yum -y update && \  
yum -y install epel-release && yum -y install nginx php php-fpm php-pecl-apcu
php-cli php-pear php-pdo php-mysqlnd php-pecl-memcache php-pecl-memcached \  
php-gd php-mbstring php-mcrypt php-xml wget tar nss_wrapper gettext supervisor
&& \  
yum clean all && \  
groupadd wordpress -g 56 && \  
useradd wordpress -u 56 -g wordpress -s /sbin/nologin -d "$NGINX_HOME" && \  
test "$(id wordpress)" = "uid=56(wordpress) gid=56(wordpress)
groups=56(wordpress)"  
  
# Download / install / configure WP  
RUN cd /var/www && \  
wget -nv https://wordpress.org/latest.tar.gz && \  
tar xvfa latest.tar.gz && \  
  
# PHP config edits  
sed -i 's|;cgi.fix_pathinfo=1|cgi.fix_pathinfo=0|'g /etc/php.ini && \  
sed -i 's|post_max_size = 8M|post_max_size = 100M|'g /etc/php.ini && \  
sed -i 's|upload_max_filesize = 8M|upload_max_filesize = 100M|'g /etc/php.ini
&& \  
  
# FPM config edits  
sed -i 's|error_log = /var/log/php-fpm/error.log|error_log = /tmp/php-
fpm_error.log|'g /etc/php-fpm.conf && \  
sed -i '1s/^/pid = \/tmp\/php-fpm.pid \n/' /etc/php-fpm.d/www.conf && \  
  
# FPM conf.d www config edits  
  
sed -i 's|listen = 127.0.0.1:9000|listen = '\/var\/run\/php-fpm\/php-
fpm.sock'|'g /etc/php-fpm.d/www.conf && \  
sed -i 's|user = apache|user = wordpress|'g /etc/php-fpm.d/www.conf && \  
sed -i 's|group = apache|group = wordpress|'g /etc/php-fpm.d/www.conf && \  
sed -i 's|listen.allowed_clients = 127.0.0.1||g' /etc/php-fpm.d/www.conf && \  
echo "listen.mode = 660" >> /etc/php-fpm.d/www.conf  
  
RUN chown -R wordpress.0 $NGINX_HOME && \  
chmod -R g+rwx $NGINX_HOME && \  
chown -R wordpress.0 /var/lib/nginx && \  
chmod -R ug+rwx /var/lib/nginx && \  
chown -R wordpress.0 /var/run/php-fpm && \  
chmod -R 777 /var/run/php-fpm  
  
WORKDIR $NGINX_HOME  
EXPOSE 8080  
# Add config  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisord.conf  
ADD passwd.template /tmp/passwd.template  
  
COPY ./start.sh /start.sh  
RUN chown -R wordpress.0 /start.sh && \  
chmod 770 /start.sh  
  
USER 56  
VOLUME ["/var/www/wordpress"]  
ENTRYPOINT [ "/start.sh" ]  


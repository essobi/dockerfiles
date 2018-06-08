FROM militarycars/sugar-docker-amazon-linux-2-image  
LABEL author=magarenz@militarycars.com  
  
COPY config/httpd.conf /etc/httpd/conf/httpd.conf  
  
RUN adduser ec2-user  
  
RUN ln -sfT /dev/stderr "$HTTPD_LOG_DIR/error.log" \  
&& ln -sfT /dev/stdout "$HTTPD_LOG_DIR/access.log" \  
&& ln -sfT /dev/stdout "$HTTPD_LOG_DIR/other_vhosts_access.log"  
  
RUN sed -i "s#memory_limit = .*#memory_limit = 512M#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#.*date.timezone =.*#date.timezone = America/New_York#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#post_max_size = .*#post_max_size = 100M#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#upload_max_filesize = .*#upload_max_filesize = 100M#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#max_execution_time = .*#max_execution_time = 600#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#max_input_time = .*#max_input_time = 600#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#error_reporting = .*#error_reporting = E_ALL \& ~E_NOTICE \&
~E_STRICT \& ~E_DEPRECATED#" /etc/opt/remi/php71/php.ini \  
&& sed -i "s#;error_log = syslog#error_log = /var/log/httpd/error_log#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#;realpath_cache_size = .*#realpath_cache_size = 512k#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#;realpath_cache_ttl = .*#realpath_cache_ttl = 600#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#session.save_handler = .*#session.save_handler = redis#"
/etc/opt/remi/php71/php.ini \  
&& sed -i 's#;session.save_path = .*#session.save_path = "tcp://sugar-
redis:6379"#' /etc/opt/remi/php71/php.ini \  
&& sed -i "s#.*date.timezone =.*#date.timezone = America/New_York#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#error_reporting = .*#error_reporting = E_ALL \& ~E_NOTICE \&
~E_STRICT \& ~E_DEPRECATED#" /etc/opt/remi/php71/php.ini \  
&& sed -i "s#;error_log = syslog#error_log = /proc/1/fd/1#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#display_errors = Off#display_errors = On#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#;realpath_cache_size = .*#realpath_cache_size = 512k#"
/etc/opt/remi/php71/php.ini \  
&& sed -i "s#;realpath_cache_ttl = .*#realpath_cache_ttl = 600#"
/etc/opt/remi/php71/php.ini  
  
RUN curl -sS http://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
WORKDIR "/var/www/html/sugarcrm"  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]


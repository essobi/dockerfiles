FROM militarycars/sugar-docker-amazon-linux-2-image  
LABEL author=magarenz@militarycars.com  
  
RUN yum install -y sudo  
  
RUN adduser ec2-user  
RUN echo "ec2-user ALL=NOPASSWD: ALL" > /etc/sudoers.d/ec2-user  
  
RUN sed -i "s#.*date.timezone =.*#date.timezone = America/New_York#"
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
  
COPY apps/sugarcron /usr/local/bin/sugarcron  
RUN chmod +x /usr/local/bin/sugarcron  
  
WORKDIR "/var/www/html/sugarcrm"  
USER ec2-user  
CMD ["/usr/local/bin/sugarcron"]


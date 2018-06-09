FROM referup/apache:latest  
  
MAINTAINER Juan Carlos Moreno <juancarlos.moreno@ackstorm.com>  
LABEL name="eu.gcr.io/talent-clue/referup-engine-nginx"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install supervisor-stdout  
RUN \  
apt-get update && \  
apt-get install -y python-pip && \  
pip install supervisor-stdout && \  
rm -rf /var/lib/apt/lists/*  
  
# Install add-apt-repository  
RUN apt-get update && \  
apt-get install -y --no-install-recommends software-properties-common && \  
rm -rf /var/lib/apt/lists/*  
  
# Add stable ppa  
RUN add-apt-repository ppa:nginx/stable  
  
# Install nginx  
RUN apt-get update && \  
apt-get install -y --no-install-recommends supervisor ca-certificates nginx
nginx-extras lua-socket && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# Clean config  
RUN rm -Rf /var/www/*  
RUN rm -Rf /etc/nginx/sites-enabled/default.conf  
  
# Copy code  
RUN mkdir -p /var/www/html  
  
# Copy configs  
COPY conf/php5/fpm /etc/php5/fpm  
COPY conf/nginx /etc/nginx  
COPY conf/supervisor /etc/supervisor  
# Estas líneas hacen que no funcione el site  
#COPY conf/nginx/conf.d /etc/nginx/  
#COPY conf/nginx/fastcgi_params /etc/nginx/  
#COPY conf/nginx/koi-utf /etc/nginx/  
#COPY conf/nginx/koi-win /etc/nginx/  
#COPY conf/nginx/mime.types /etc/nginx/  
#COPY conf/nginx/nginx.conf /etc/nginx/  
#COPY conf/nginx/win-utf /etc/nginx/  
# Opcache tunning  
COPY conf/php5/mods/referup-opcache.ini /etc/php5/mods-available/  
RUN php5enmod -s ALL referup-opcache  
  
# Enable xdebug  
RUN echo 'zend_extension=/usr/lib/php5/20121212/xdebug.so\n\  
xdebug.idekey=IDKEY\n\  
xdebug.remote_enable=1\n\  
xdebug.remote_connect_back=1\n'\  
>> /etc/php5/fpm/php.ini  
RUN chmod +x /usr/lib/php5/20121212/xdebug.so  
  
# Copy ENV var hack to php-fpm  
COPY scripts/start_phpfpm_with_env.sh /root  
  
# App config  
RUN mkdir /var/cache/nginx  
RUN mkdir /var/log/php5-fpm; chown www-data /var/log/php5-fpm  
  
# Create log path for simplesaml  
RUN mkdir /var/log/simplesaml; chown www-data /var/log/simplesaml  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stderr /var/log/php5-fpm/fpm-error.log  
RUN ln -sf /dev/stderr /var/log/php5-fpm/www-error.log  
RUN ln -sf /dev/stdout /var/log/php5-fpm/www-access.log  
RUN ln -sf /dev/stdout /var/log/php5-fpm/www-slow.log  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN php5dismod -s ALL referup-newrelic  
  
EXPOSE 80  
WORKDIR "/var/www/html"  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  


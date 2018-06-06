FROM ricktap/icinga2-base:latest  
  
ENV ICINGA_WEB_VERSION 2.4.1  
# install nginx  
RUN apt-get update && \  
apt-get install -y curl ca-certificates nginx gettext-base && \  
apt-get install -y php5 php5-cli php5-fpm php5-intl php5-imagick php5-gd
php5-mysql php5-curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# link the nginx logs to stdout/-err  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# install icinga2-web  
RUN curl -sSL
"https://github.com/Icinga/icingaweb2/archive/v${ICINGA_WEB_VERSION}.tar.gz" |
tar xz -C /opt  
RUN ln -s "/opt/icingaweb2-${ICINGA_WEB_VERSION}" "/opt/icingaweb2"  
WORKDIR "/opt/icingaweb2"  
  
# configure nginx  
COPY src/nginx-default /opt/nginx-default.template  
RUN ICINGA_WEB_LOCATION=$(bin/icingacli setup config webserver nginx
--document-root /opt/icingaweb2/public) && \  
export ICINGA_WEB_LOCATION && \  
envsubst < /opt/nginx-default.template > /etc/nginx/sites-enabled/default && \  
sed -i 's/;date.timezone =/date.timezone = Europe\/Berlin/'
/etc/php5/fpm/php.ini  
  
# user management  
RUN addgroup --system icingaweb2 && \  
usermod -a -G icingaweb2 www-data  
  
# create configuration directories and setup the token  
RUN ./bin/icingacli setup config directory --group icingaweb2
--config=/webconfig && \  
ln -s /webconfig /etc/icingaweb2  
  
# expose the web ports  
EXPOSE 80 443  
VOLUME /webconfig  
VOLUME /config  
  
# setup start scripts  
RUN mkdir -p /etc/my_init.d  
COPY src/run.sh /etc/my_init.d/20_run.sh  
RUN chmod +x /etc/my_init.d/*.sh  
  
# set the start command  
CMD ["/sbin/my_init"]  


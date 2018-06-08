FROM romeoz/docker-nginx-php:5.6  
# Setup environment variables for initializing New Relic  
ENV NR_INSTALL_SILENT 1  
ENV NR_INSTALL_KEY **ChangeMe**  
ENV NR_APP_NAME "Default App Name"  
RUN \  
echo 'deb http://pkg.cloudflare.com/ xenial main' | tee -a
/etc/apt/sources.list.d/cloudflare-main.list \  
&& curl -C - https://pkg.cloudflare.com/pubkey.gpg | apt-key add - \  
&& echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee -a
/etc/apt/sources.list.d/newrelic-main.list \  
&& curl -C - https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& apt-get update \  
&& apt-get install -y git railgun-stable newrelic-php5 php-memcached \  
&& apt-get autoremove -y && apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
EXPOSE 2408  
ADD sysctl.conf /etc/sysctl.conf  
ADD limits.conf /etc/security/limits.conf  
RUN echo "session required pam_limits.so" >> /etc/pam.d/common-session  
ADD www.conf /etc/php5/fpm/pool.d/www.conf  
ADD railgun.sh /bin/  
ADD newrelic.sh /bin/  
ADD entrypoint.sh /bin/  
RUN chmod +x /bin/*.sh  
CMD ["/bin/entrypoint.sh"]  


FROM ubuntu:14.04  
MAINTAINER dev@cedvan.com  
  
# Install requirements  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
curl \  
wget \  
ca-certificates \  
unzip  
  
# Install PHP and Nginx  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
cron \  
git \  
php5-cli \  
php5-intl \  
php5-curl \  
nginx \  
openssh-client  
  
# Configure PHP and Nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i "s/;date.timezone.*/date.timezone = Europe\/Paris/"
/etc/php5/cli/php.ini \  
&& rm -f /etc/nginx/sites-enabled/default \  
&& rm -f /etc/nginx/sites-available/default  
  
# Vhosts  
COPY assets/vhosts /etc/nginx/sites-available  
  
# Install satis  
RUN cd /opt \  
&& curl -sS https://getcomposer.org/installer | php \  
&& php composer.phar create-project composer/satis --stability=dev --keep-vcs
\  
&& rm -f composer.phar  
  
# Scripts bash satis  
COPY assets/bin /bin/satis/  
RUN chmod u+x /bin/satis/* \  
&& echo "0 * * * * root /bin/satis/launch.sh" >> /etc/crontab  
  
#Configure SSH  
RUN mkdir -p /root/.ssh \  
&& sed -i "s/# StrictHostKeyChecking ask/ StrictHostKeyChecking no/"
/etc/ssh/ssh_config  
  
VOLUME /root/.ssh  
  
WORKDIR /var/www  
  
EXPOSE 80  
EXPOSE 443  
CMD /bin/satis/launch.sh && /etc/init.d/cron start && nginx -c
/etc/nginx/nginx.conf  


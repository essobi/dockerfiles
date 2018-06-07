FROM phusion/baseimage:0.9.19  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
curl unzip \  
php php-curl php-zip php-pdo php-gd php-xml php-apcu php-mysql php-intl \  
nginx-light \  
ffmpeg  
  
RUN mkdir /run/php /etc/service/nginx /etc/service/php /opt/tmp && \  
chown www-data /opt/tmp  
  
ADD services/nginx /etc/service/nginx/run  
ADD services/php /etc/service/php/run  
ADD services/cron /etc/cron.d/ktv  
  
ADD misc/bashrc /root/bashrc  
ADD misc/init /etc/my_init.d/00_my_init  
  
RUN echo "source /root/bashrc" >> ~/.bashrc && \  
chmod 600 /etc/cron.d/ktv  
  
RUN mkdir -p /opt/ktv/fs/cache /var/lib/php/session && \  
chown www-data:www-data -R /opt/ktv/fs /var/lib/php/session  
  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/php.ini /etc/php/7.0/fpm/php.ini  
ADD config/php.ini /etc/php/7.0/cli/php.ini  
ADD config/pool.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN rm -rf /etc/service/{sshd,syslog-forwarder,syslog-ng} && \  
rm -rf /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
EXPOSE 80  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV STAGE_ENV=prod  
  
WORKDIR /var/www


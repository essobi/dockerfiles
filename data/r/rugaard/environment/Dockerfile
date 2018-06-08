FROM ubuntu:16.04  
LABEL maintainer="Morten Rugaard <morten@rugaard.me>" version="1.0.0"  
  
# Copy configuration files.  
COPY ./config /docker/config/  
RUN chmod +x /docker/config/*  
  
# Copy helper files.  
COPY ./helpers /docker/helpers/  
RUN chmod +x /docker/config/*  
  
# Copy install scripts.  
COPY ./install /docker/install/  
RUN chmod +x /docker/install/*  
  
# Copy setup files.  
COPY ./setup /docker/setup/  
RUN chmod +x /docker/setup/*  
  
# Copy entrypoint.  
COPY ./entrypoint.sh /docker/entrypoint.sh  
RUN chmod +x /docker/entrypoint.sh  
  
# Regional settings.  
ENV ENCODING UTF-8  
ENV LOCALE da_DK  
ENV TZ Europe/Copenhagen  
  
# Make Ubuntu Dockerable.  
ENV RUNLEVEL 1  
ENV DEBIAN_FRONTEND noninteractive  
RUN /docker/install/prepare.sh  
  
# Core packages.  
RUN /docker/install/packages.sh  
  
# Supervisor.  
ENV SUPERVISORD_USER admin  
ENV SUPERVISORD_PASSWORD secret  
RUN /docker/install/supervisor.sh  
  
# Cron.  
RUN /docker/install/cron.sh  
  
# MariaDB.  
ENV MYSQL_USER admin  
ENV MYSQL_PASSWORD secret  
ENV MYSQL_DATABASE development  
RUN /docker/install/mariadb.sh  
  
# PHP.  
RUN /docker/install/php.sh  
  
# Composer.  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN /docker/install/composer.sh  
  
# Redis.  
ENV REDIS_UI_USER admin  
ENV REDIS_UI_PASSWORD secret  
RUN /docker/install/redis.sh  
  
# Beanstalk.  
ENV BEANSTALKD_UI_USER admin  
ENV BEANSTALKD_UI_PASSWORD secret  
RUN /docker/install/beanstalk.sh  
  
# phpMyAdmin.  
RUN /docker/install/phpmyadmin.sh  
  
# Nginx.  
RUN /docker/install/nginx.sh  
  
# Node.js.  
RUN /docker/install/nodejs.sh  
  
# Housekeeping.  
RUN /docker/install/housekeeping.sh  
  
# Set working directory.  
WORKDIR /var/www  
  
# 80 = HTTP  
# 3306 = MySQL  
# 3310 = phpMyAdmin  
# 6379 = Redis  
# 6380 = Redis Web UI  
# 9001 = Supervisor Web UI  
# 11300 = Beanstalk  
# 11350 = Beanstalk Web UI  
EXPOSE 80 3306 3310 6379 6380 9001 11300 11350  
# Set entrypoint.  
ENTRYPOINT ["/docker/entrypoint.sh"]  
  
# Execute init command.  
CMD ["init"]


FROM zolotoykod/web:latest  
LABEL maintainer="Constantine Karnaukhov <genteelknight@gmail.com>"  
# install cron and crontab job  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install cron \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/* \  
&& echo "service cron restart" >> /usr/local/sbin/entrypoint \  
&& echo "*/5 * * * * /usr/bin/php -f
/var/www/html/bitrix/modules/main/tools/cron_events.php" | crontab  
COPY nginx/ /etc/nginx/  
COPY www/ /var/www/html/  
  
# Clean working directory of demo files  
ONBUILD RUN rm -rf ./*  


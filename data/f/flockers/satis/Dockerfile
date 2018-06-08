FROM ypereirareis/docker-satis:4.2  
  
RUN composer self-update \  
&& composer global require "hirak/prestissimo:^0.3"  
RUN rm /etc/cron.d/satis-cron  
  
COPY startup.sh /app/scripts/startup.sh  
COPY build.sh /app/scripts/build.sh  
RUN chmod 777 /app/config.json \  
&& chmod 777 /app/server.js \  
&& chmod 777 /app/scripts/startup.sh \  
&& chmod 777 /app/scripts/build.sh  


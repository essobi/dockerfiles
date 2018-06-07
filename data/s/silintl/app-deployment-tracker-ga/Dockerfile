FROM silintl/php7:latest  
  
WORKDIR /data  
  
COPY composer.json /data/composer.json  
RUN composer install --no-scripts --no-plugins  
  
COPY bin/ /data/bin  
COPY src/ /data/src  
RUN touch /data/.env  
  
ENTRYPOINT ["/data/bin/track-deployment"]  
CMD ["true"]


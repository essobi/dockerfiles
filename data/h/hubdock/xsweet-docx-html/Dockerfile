FROM hubdock/php7-apache-saxonhe  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libz-dev \  
&& docker-php-ext-install -j$(nproc) zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
RUN mkdir /input  
VOLUME /input  
  
COPY src/ /var/www/html/  
  
COPY entrypoint.sh entrypoint.sh  
RUN chmod +x entrypoint.sh  
  
COPY update.php update.php  
  
ENTRYPOINT ["./entrypoint.sh"]  


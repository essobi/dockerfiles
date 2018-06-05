FROM thruio/docker-webapp:php7  
  
RUN add-apt-repository ppa:mc3man/trusty-media && \  
apt-get update && \  
apt-get -yq install \  
livemedia-utils \  
ffmpeg && \  
git clone https://github.com/nginx/nginx.git -b release-1.5.5 /tmp/nginx  
  
RUN wget http://nginx.org/download/nginx-1.9.12.tar.gz && \  
tar -xzf nginx-1.9.12.tar.gz && \  
rm /tmp/nginx -R && \  
mv nginx-1.9.12 /tmp/nginx  
  
ADD . /app  
RUN composer install  
  
EXPOSE 8090  
# Add startup scripts  
RUN mkdir /etc/service/ffserver  
ADD run.camera-monitor.sh /etc/service/monitor/run  
ADD run.ffserver.sh /etc/service/ffserver/run  
RUN chmod +x /etc/service/*/run  
  
RUN sed -i "s/disable_functions.*/;disable_functions = /g"
/etc/php/7.0/cli/php.ini


FROM wordpress  
  
COPY wp-content /var/www/html/wp-content  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
ffmpeg \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo upload_max_filesize=500M > /usr/local/etc/php/conf.d/uploads.ini \  
&& echo post_max_size=500M >> /usr/local/etc/php/conf.d/uploads.ini  
  


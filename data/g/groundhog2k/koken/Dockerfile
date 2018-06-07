FROM alpine:latest  
MAINTAINER Goeran Poehner "goeran.poehner@gmail.com"  
LABEL Description="Koken docker image"  
ARG TIMEZONE_ARG=Universal  
  
WORKDIR /  
ENV TIMEZONE=${TIMEZONE_ARG}  
RUN apk update && apk upgrade && apk add tzdata nginx php5-fpm php5-zlib
php5-json php5-gd php5-mysql php5-openssl php5-mcrypt php5-curl graphicsmagick
imagemagick ffmpeg ca-certificates openssl  
COPY configs/default.conf /etc/nginx/conf.d  
RUN wget https://s3.amazonaws.com/koken-installer/releases/Koken_Installer.zip  
RUN mkdir -p /var/www/koken  
RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime  
RUN echo "${TIMEZONE}" > /etc/timezone  
RUN mkdir -p /run/nginx && mkdir -p /run/php-fpm5  
  
RUN sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i"
/etc/php5/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 101M/g"
/etc/php5/php.ini  
  
RUN sed -i -e "s/client_max_body_size.*$/client_max_body_size
100m;\n\tport_in_redirect off;/" /etc/nginx/nginx.conf  
RUN sed -i -e "s/#gzip on;/gzip on;/" /etc/nginx/nginx.conf  
  
RUN sed -i -e "s#listen\s*=\s*127.0.0.1:9000#listen = /var/run/php5-fpm.sock#"
/etc/php5/php-fpm.conf  
RUN sed -i -e "s#user\s*=\s*nobody#user = nginx#" /etc/php5/php-fpm.conf  
RUn sed -i -e "s#group\s*=\s*nobody#group = nginx#" /etc/php5/php-fpm.conf  
RUN sed -i -e "s#;listen.owner\s*=\s*nobody#listen.owner = nginx#"
/etc/php5/php-fpm.conf  
RUN sed -i -e "s#;listen.group\s*=\s*nobody#listen.group = nginx#"
/etc/php5/php-fpm.conf  
RUN sed -i -e "s#;listen.mode\s*=\s*0660#listen.mode = 0660#" /etc/php5/php-
fpm.conf  
RUN sed -i -e "s/;pm.max_requests\s*=\s*500/pm.max_requests = 500/g"
/etc/php5/php-fpm.conf  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN apk del tzdata  
COPY scripts/start.sh /usr/local/bin  
  
EXPOSE 80  
VOLUME /var/www/koken  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]  


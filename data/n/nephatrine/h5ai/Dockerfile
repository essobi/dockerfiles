FROM nephatrine/base-php7:latest  
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"  
  
RUN echo "====== RUNTIME CONFIGURATION ======" \  
&& apk \--update upgrade \  
&& apk add \  
ffmpeg \  
imagemagick \  
zip \  
&& mkdir -p /mnt/media \  
\  
&& echo "====== BUILD CONFIGURATION ======" \  
&& apk add \--virtual .build-h5ai \  
nodejs-npm \  
\  
&& echo "====== INSTALL H5AI ======" \  
&& cd /usr/src \  
&& git clone https://github.com/lrsjng/h5ai.git && cd h5ai \  
&& npm install && npm run build \  
&& unzip build/*.zip -d /var/www/html/ \  
\  
&& echo "====== CONFIGURE NGINX ======" \  
&& sed -i 's~index.html~index.html /_h5ai/public/index.php~g'
/etc/nginx/nginx.conf \  
\  
&& echo "====== CONFIGURE PHP-FPM ======" \  
&& sed -i 's~/mnt/config/www/~/mnt/config/www/:/mnt/media/~g' /etc/php/php-
fpm.d/www.conf \  
\  
&& echo "====== CLEANUP ======" \  
&& cd /usr/src \  
&& apk del \--purge .build-h5ai \  
&& rm -rf \  
/tmp/* \  
/usr/src/* \  
/var/cache/apk/*  
  
COPY override /


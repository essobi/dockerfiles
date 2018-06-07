FROM alpine:3.7  
# Load ash profile on launch  
ENV ENV="/etc/profile"  
# Set the timezone  
ENV TIMEZONE America/New_York  
  
# configure our PHP limits  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 50  
ENV PHP_MAX_POST 100M  
  
# Setup ash profile prompt and my old man alias  
# Create work directory  
RUN mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh && \  
echo alias dir=\'ls -alh --color\' >> /etc/profile && \  
mkdir -p /app /run/nginx /run/php7  
  
# install php7-fpm and a db extension  
RUN apk --update --no-cache add nginx php7-fpm dumb-init tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk del tzdata  
  
# Setup the www-data user  
# Working?  
# RUN addgroup -g 82 -S www-data && \  
RUN adduser -u 82 -D -S -G www-data www-data  
  
# Manually make some changes for the PHP.INI file  
RUN sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i"
/etc/php7/php.ini && \  
sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i"
/etc/php7/php.ini && \  
sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i"
/etc/php7/php.ini && \  
sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i"
/etc/php7/php.ini && \  
sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i"
/etc/php7/php.ini && \  
sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php7/php.ini && \  
sed -i "s|;*error_log = .*|error_log = \/proc\/self\/fd\/1|i"
/etc/php7/php.ini  
  
# own the run directory so php can save it's pid and socket  
RUN chown www-data /run/php7/  
  
# copy our config files over to the container  
COPY ./configs/php-fpm.conf /etc/php7/php-fpm.conf  
COPY ./configs/nginx.conf /etc/nginx/nginx.conf  
COPY ./configs/default.conf /etc/nginx/conf.d/default.conf  
  
# setup our working directory  
WORKDIR /app  
COPY ./code .  
  
# download and set the user/pass pair for wordpress  
# ADD https://wordpress.org/latest.tar.gz .  
RUN chown -R www-data:www-data /app  
  
# expose our service port  
EXPOSE 80  
# start with our PID 1 controller  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
# what we use to start the container  
CMD ["/bin/sh", "-c", "php-fpm7 --daemonize && nginx -g \"daemon off;\""]  


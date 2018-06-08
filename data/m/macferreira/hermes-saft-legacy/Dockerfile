FROM nginx:1.11.3  
# App env vars  
ENV DB_CONN_SERVERNAME localhost  
ENV DB_CONN_DATABASE pos  
ENV DB_CONN_USERNAME dummy  
ENV DB_CONN_PASSWORD dummy-password  
  
# Copy nginx conf  
COPY docker/prod/http/default.conf /etc/nginx/conf.d/default.conf  
  
# Update cache and install PHP  
RUN apt-get update && apt-get -y install \  
php5-fpm \  
php5-cli \  
php5-mysql \  
php5-dev && \  
sed -i -e "s/listen = \/var\/run\/php5-fpm.sock/listen = 127.0.0.1:9000/g"
/etc/php5/fpm/pool.d/www.conf  
  
# Copy in code  
ADD ./src /var/www/html/  
  
EXPOSE 80  
# Add the startup script and run it  
ADD docker/prod/run-script/run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
CMD /root/run.sh


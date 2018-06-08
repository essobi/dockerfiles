FROM alpine:latest  
MAINTAINER wrfly <mr.wrfly@gmail.com>  
  
# Install PHP  
RUN apk --update add php5 && \  
sed -i "s/track_errors\ =\ Off/track_errors\ =\ On/g" /etc/php5/php.ini && \  
sed -i "s/display_errors\ =\ Off/display_errors\ =\ On/g" /etc/php5/php.ini  
  
EXPOSE 80  
COPY app /app  
COPY fc-init.sh /  
RUN chmod +x fc-init.sh  
CMD ["/fc-init.sh"]  


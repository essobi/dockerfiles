FROM alpine:edge  
  
RUN apk --update add nginx php5-fpm && \  
mkdir -p /run/nginx  
  
ADD www /www  
ADD nginx.conf /etc/nginx/  
ADD php-fpm.conf /etc/php5/php-fpm.conf  
ADD run.sh /run.sh  
  
ENV LISTEN_PORT=80  
EXPOSE 80  
CMD /run.sh  


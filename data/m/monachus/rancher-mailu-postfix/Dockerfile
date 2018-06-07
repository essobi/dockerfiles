FROM alpine:latest  
  
RUN apk add --no-cache bash postfix postfix-sqlite postfix-pcre rsyslog
supervisor  
  
COPY docker_files/conf /etc/postfix  
COPY docker_files/rsyslog.conf /etc/rsyslog.conf  
COPY docker_files/listen.conf /etc/rsyslog.d/listen.conf  
COPY docker_files/supervisord.conf /etc/supervisord.conf  
COPY start.sh /start.sh  
  
CMD ["/start.sh"]  


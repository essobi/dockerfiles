FROM alpine:3.6  
RUN apk add --no-cache --update postfix ca-certificates supervisor rsyslog
bash \  
&& rm -rf /var/cache/apk/*  
  
COPY files/supervisord.conf /etc/supervisord.conf  
COPY files/rsyslog.conf /etc/rsyslog.conf  
  
VOLUME [ "/etc/postfix", "/var/mail", "/var/spool/postfix" ]  
  
USER root  
WORKDIR /tmp  
  
EXPOSE 25 587  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]  


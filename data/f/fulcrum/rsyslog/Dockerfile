FROM fulcrum/alpine  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
# from https://github.com/voxxit/dockerfiles/tree/master/rsyslog  
RUN apk add --update rsyslog \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 514 514/udp  
  
VOLUME [ "/var/log", "/etc/rsyslog.d" ]  
  
# for some reason, the apk comes built with a v5  
# config file. using this one for v8:  
COPY ./etc/rsyslog.conf /etc/rsyslog.conf  
  
ENTRYPOINT [ "rsyslogd", "-n" ]  


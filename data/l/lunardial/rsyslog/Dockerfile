FROM alpine:latest  
MAINTAINER Tomoyuki Sugimura <tomoyuki.sugimura@gmail.com>  
  
RUN apk update --no-cache \  
&& apk add --no-cache rsyslog  
  
COPY rsyslog.conf /etc/rsyslog.conf  
  
ENTRYPOINT [ "rsyslogd", "-n" ]  


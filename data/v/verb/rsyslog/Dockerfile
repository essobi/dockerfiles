FROM alpine:3.2  
MAINTAINER Lee Verberne <lee@blarg.org>  
  
RUN apk add --update rsyslog && rm -rf /var/cache/apk/*  
  
CMD ["rsyslogd", "-n", "-f", "/etc/rsyslog.conf"]  


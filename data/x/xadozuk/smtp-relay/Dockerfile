FROM alpine:3.3  
MAINTAINER Xadozuk <xadozuk@gmail.com>  
  
RUN apk --no-cache add postfix rsyslog supervisor bash  
COPY entrypoint postfix /  
COPY supervisor.d /etc/supervisor.d  
  
EXPOSE 25  
CMD ["/entrypoint"]  


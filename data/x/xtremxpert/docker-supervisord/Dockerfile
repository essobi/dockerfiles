FROM xtremxpert/docker-base:alpine  
  
MAINTAINER XtremXpert <xtremxpert@xtremxpert.com>  
  
RUN apk update && \  
apk upgrade && \  
apk --update add \  
supervisor \  
openssh  
  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]  


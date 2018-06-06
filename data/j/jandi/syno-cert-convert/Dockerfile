FROM alpine:latest  
  
LABEL maintainer "mail@jand.one"  
  
COPY bin/ "/usr/local/bin/"  
COPY crontab "/var/spool/cron/crontabs/root"  
  
RUN apk --update --no-cache add curl jq openssl unzip \  
&& chmod +x "/usr/local/bin/cert-convert"  
  
VOLUME ["/etc/cert-convert"]  
  
CMD crond -l 2 -f


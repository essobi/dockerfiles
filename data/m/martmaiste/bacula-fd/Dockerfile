FROM alpine:3.6  
MAINTAINER "ull <ull@dbweb.ee>  
  
RUN apk -U upgrade && apk add \  
bash \  
bacula-client  
  
RUN mkdir /etc/bacula /var/lib/bacula  
  
ADD bacula-fd.conf /etc/bacula/bacula-fd.conf  
ADD bacula-fd.conf /etc/bacula/bacula-fd.conf.orig  
  
ADD run.sh /  
  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  
EXPOSE 9102  


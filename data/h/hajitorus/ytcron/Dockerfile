FROM alpine:edge  
MAINTAINER docker.c@nsuckmyballs.com  
  
#ADD get-subs /etc/periodic/15min/get-subs  
#RUN chmod 0755 /etc/periodic/15min/get-subs  
RUN ln -s /base/15min /etc/periodic/15min/ytcron  
RUN ln -s /base/hourly /etc/periodic/hourly/ytcron  
RUN apk update \  
&& apk add ca-certificates coreutils fish youtube-dl \  
&& rm -rf /var/cache/apk/*  
RUN youtube-dl -U  
CMD crond -f && tail -f /var/log/cron.log  


FROM alpine:latest  
  
MAINTAINER Shane Starcher <shane.starcher@gmail.com>  
  
RUN apk --update add bind &&\  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
  
ENV dockerize_version=0.2.0  
RUN \  
mkdir -p /usr/local/bin/ &&\  
apk --update add curl &&\  
curl -SL
https://github.com/jwilder/dockerize/releases/download/v${dockerize_version}/dockerize-
linux-amd64-v${dockerize_version}.tar.gz \  
| tar xzC /usr/local/bin &&\  
apk del --purge curl && \  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
  
EXPOSE 53  
RUN mkdir -p /var/cache/bind  
ADD start /bin/start  
ADD named.conf.tmpl /etc/bind/named.conf.tmpl  
CMD ["/bin/start"]  


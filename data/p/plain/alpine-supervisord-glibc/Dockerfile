FROM alpine  
MAINTAINER lw6c@qq.com  
  
RUN apk update && apk add --no-cache ca-certificates openssl && update-ca-
certificates && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \  
apk add glibc-2.25-r0.apk && \  
rm glibc-2.25-r0.apk  
  
RUN apk add -u python py-pip  
RUN pip install supervisor  
COPY supervisor /etc/supervisor  
RUN mkdir /etc/supervisor/conf.d \  
&& mkdir -p /var/log/supervisor \  
&& touch /var/log/supervisor/supervisord.log  
RUN apk add -U tzdata  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisor/supervisord.conf"]  
  


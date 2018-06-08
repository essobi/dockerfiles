FROM alpine:3.6  
MAINTAINER infinityworks  
  
RUN apk --update add \  
haproxy \  
python \  
curl  
  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -o /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
COPY confd/*.tmpl /etc/confd/templates/  
COPY confd/*.toml /etc/confd/conf.d/  
COPY bin/loadbalancer.init /init  
COPY bin/haproxy-status.py /usr/local/bin  
  
RUN chmod +x /init /usr/local/bin/haproxy-status.py  
RUN mkdir -p /usr/local/etc/haproxy  
  
EXPOSE 80  
ENTRYPOINT ["/init"]  


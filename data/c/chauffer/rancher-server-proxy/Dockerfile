FROM haproxy:1.7-alpine  
MAINTAINER Simone <chaufnet@gmail.com>  
  
COPY haproxy.cfg.tmpl /usr/local/etc/haproxy/haproxy.cfg.tmpl  
  
ENV DOCKERIZE_VERSION=v0.3.0  
RUN apk --no-cache add --virtual=.build-deps wget ca-certificates && \  
update-ca-certificates && \  
wget -q -O-
https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz | tar -zxvf - -C /bin && \  
apk del .build-deps  
  
CMD ["dockerize", "-template",
"/usr/local/etc/haproxy/haproxy.cfg.tmpl:/usr/local/etc/haproxy/haproxy.cfg",
"haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  
ENV BACKEND_HOST=rancher.chauf.net \  
BACKEND_PORT=8080  


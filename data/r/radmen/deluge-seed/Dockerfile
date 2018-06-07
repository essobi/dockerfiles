FROM alpine:edge  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk add --no-cache deluge \  
py2-pip \  
gettext \  
openssl  
  
RUN pip install incremental \  
constantly \  
automat \  
service_identity  
  
RUN mkdir -p /deluge/config \  
/deluge/config/state \  
/deluge/completed \  
/deluge/downloads \  
/deluge/torrents  
  
COPY container /  
  
VOLUME /deluge/completed  
  
EXPOSE 8112  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


FROM alpine  
  
ENV CONFD_VERSION=0.12.0-alpha3  
  
RUN apk add --no-cache curl \  
&& curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& mkdir -p /postgres-c2c-conf/docker-entrypoint-initdb.d  
  
COPY ./docker-entrypoint.sh /postgres-c2c-conf/docker-entrypoint.sh  
COPY ./docker-entrypoint.d/ /postgres-c2c-conf/docker-entrypoint.d/  
COPY ./docker-entrypoint-initdb.d/ /postgres-c2c-conf/docker-entrypoint-
initdb.d/  
  
COPY ./conf.d/ /etc/confd/conf.d/  
COPY ./templates/ /etc/confd/templates/  
  
VOLUME [ "/postgres-c2c-conf" ]  
  
ENTRYPOINT ["confd"]  
CMD ["-onetime", "-backend", "rancher", "-prefix", "/2015-12-19"]  


FROM alpine:edge  
  
ENV KAPACITOR_VERSION 1.2.0  
RUN apk add --no-cache --virtual .build-deps wget gnupg tar ca-certificates &&
\  
update-ca-certificates && \  
wget -q https://github.com/allen13/kapacitor-docker-
custom/releases/download/v1.2.0/kapacitor-${KAPACITOR_VERSION}-static_linux_amd64.tar.gz
&& \  
mkdir -p /usr/src && \  
tar -C /usr/src -xzf kapacitor-${KAPACITOR_VERSION}-static_linux_amd64.tar.gz
&& \  
rm -f /usr/src/kapacitor-*/kapacitor.conf && \  
chmod +x /usr/src/kapacitor-*/* && \  
cp -a /usr/src/kapacitor-*/* /usr/bin/ && \  
rm -rf *.tar.gz* /usr/src /root/.gnupg && \  
apk del .build-deps  
  
ENV DOCKERIZE_VERSION 0.2.0  
RUN \  
apk add --no-cache curl && \  
mkdir -p /usr/local/bin/ &&\  
curl -SL
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
| tar xzC /usr/local/bin  
  
RUN mkdir -p /etc/kapacitor  
COPY kapacitor.tmpl /etc/kapacitor  
  
EXPOSE 9092  
VOLUME /var/lib/kapacitor  
  
ENV KAPACITOR_HOSTNAME kapacitor  
  
ENV INFLUXDB_HOST influxdb  
ENV INFLUXDB_USER metrics  
ENV INFLUXDB_PASSWORD metrics  
  
ENV INFLUXDB_SUBSCRIPTIONS_ENABLED false  
ENV INFLUXDB_SUBSCRIPTION_DB metrics  
ENV INFLUXDB_SUBSCRIPTION_DB_RP default  
  
ENV ALERTA_ENABLED true  
ENV ALERTA_API_URL https://golerta:5608  
ENV ALERTA_TOKEN ""  
ENV ALERTA_TOKEN_PREFIX Bearer  
  
CMD dockerize \  
-template /etc/kapacitor/kapacitor.tmpl:/etc/kapacitor/kapacitor.conf \  
kapacitord -config /etc/kapacitor/kapacitor.conf  


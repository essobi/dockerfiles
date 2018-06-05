FROM alpine  
ENV KIBANA_VERSION 4.0.3  
RUN apk upgrade --update && \  
apk add wget tar ca-certificates nodejs && \  
wget --no-check-certificate
https://download.elastic.co/kibana/kibana/kibana-$KIBANA_VERSION-
linux-x64.tar.gz -O /tmp/kibana-$KIBANA_VERSION-linux-x64.tar.gz && \  
[ -d /opt ] || mkdir /opt && \  
tar -C /opt -xzf /tmp/kibana-$KIBANA_VERSION-linux-x64.tar.gz && \  
ln -s /opt/kibana-$KIBANA_VERSION-linux-x64 /opt/kibana && \  
rm -r /tmp/* /opt/kibana/node && \  
apk del --purge wget tar ca-certificates  
RUN sed -i 's/NODE=.*/NODE=$(which node)/g' /opt/kibana/bin/kibana  
COPY ./docker-entrypoint.sh /entrypoint.sh  
COPY ./gosu /usr/local/bin/gosu  
WORKDIR /opt/kibana  
EXPOSE 5601  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["kibana"]  
  


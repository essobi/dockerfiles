FROM alpine:latest  
  
ENV CEREBRO_VERSION="0.7.3" \  
ES_ADDRESS="localhost" \  
ES_PORT="9200" \  
ES_NAME="elasticsearch"  
  
RUN \  
apk add \--update bash openjdk8 openssl && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* && \  
wget -O /tmp/cerebro-${CEREBRO_VERSION}.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
&& \  
mkdir -p /opt/cerebro && \  
cd /tmp/ && tar zxvf cerebro-${CEREBRO_VERSION}.tgz \--strip-components 1 -C
/opt/cerebro && \  
rm -rf /tmp/cerebro-${CEREBRO_VERSION}.tgz && rm /opt/cerebro/bin/cerebro.bat
&& \  
chmod 7777 /tmp/  
  
ADD container-files /  
  
ENTRYPOINT [ "/bootstrap.sh" ]  
  


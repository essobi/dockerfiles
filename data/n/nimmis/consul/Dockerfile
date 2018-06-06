FROM alpine:3.5  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
ENV DNS_RESOLVES=consul \  
DNS_PORT=8600 \  
DATACENTER=DC \  
CONSUL_VERSION=0.8.5  
COPY docker-entrypoint.sh /  
  
RUN apk update && apk upgrade && \  
  
# Make info file about this build  
mkdir -p /etc/BUILDS/ && \  
printf "Build of nimmis/consul:${CONSUL_VERSION}, date: %s\n" `date -u
+"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/consul && \  
  
# get curl  
apk add curl gnupg libcap openssl&& \  
  
# download consul  
curl -sSL
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
-o xx.zip && \  
  
# download web-ui  
  
curl -sSL
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip
-o ui.zip && \  
  
# unpack consul, webui and clean up  
unzip xx.zip && \  
mv consul /usr/local/bin/ && \  
  
# unpack web_ui  
mkdir -p /ui && \  
unzip ui.zip -d /ui && \  
  
# clean ip  
rm xx.zip ui.zip && \  
  
  
  
# remove cached info  
rm -rf /var/cache/apk/*  
  
# expose consul ports  
VOLUME [ "/data" ]  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  


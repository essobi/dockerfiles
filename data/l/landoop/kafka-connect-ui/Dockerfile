FROM alpine  
MAINTAINER Marios Andreopoulos <marios@landoop.com>  
  
WORKDIR /  
# Add needed tools  
RUN apk add --no-cache ca-certificates wget \  
&& echo "progress = dot:giga" | tee /etc/wgetrc  
  
# Add and Setup Caddy webserver  
RUN wget
"https://github.com/mholt/caddy/releases/download/v0.10.11/caddy_v0.10.11_linux_amd64.tar.gz"
-O /caddy.tgz \  
&& mkdir caddy \  
&& tar xzf caddy.tgz -C /caddy \  
&& rm -f /caddy.tgz  
  
# Add and Setup Kafka Connect UI  
ENV KAFKA_CONNECT_UI_VERSION="0.9.4"  
RUN wget "https://github.com/Landoop/kafka-connect-
ui/releases/download/v.${KAFKA_CONNECT_UI_VERSION}/kafka-connect-
ui-${KAFKA_CONNECT_UI_VERSION}.tar.gz" -O /kafka-connect-ui.tar.gz \  
&& mkdir /kafka-connect-ui \  
&& tar xzf /kafka-connect-ui.tar.gz -C /kafka-connect-ui \  
&& rm -f /kafka-connect-ui.tar.gz  
  
# Add configuration and runtime files  
ADD Caddyfile /caddy/Caddyfile.template  
ADD run.sh /  
RUN chmod +x /run.sh  
  
EXPOSE 8000  
ENTRYPOINT ["/run.sh"]  


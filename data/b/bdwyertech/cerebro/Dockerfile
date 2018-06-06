FROM openjdk:alpine  
  
ENV CEREBRO_VERSION 0.7.2  
ENV CONFD_VERSION 0.15.0  
RUN apk update && apk upgrade \  
&& apk add --no-cache bash su-exec \  
&& mkdir -p /opt/cerebro/logs \  
&& wget -O cerebro-${CEREBRO_VERSION}.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz
\  
&& tar zxvf cerebro-${CEREBRO_VERSION}.tgz -C /opt/cerebro --strip 1 \  
&& rm cerebro-${CEREBRO_VERSION}.tgz \  
&& adduser -D -h /opt/cerebro cerebro \  
&& chown cerebro:cerebro -R /opt/cerebro \  
&& wget -O /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
  
# && mkdir -p /etc/confd/{conf.d,templates}  
# Copy in Files  
COPY ./files/ /  
  
WORKDIR /opt/cerebro  
EXPOSE 9000  
ENTRYPOINT ["/docker-entrypoint.sh"]  


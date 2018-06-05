#FROM benyoo/alpine:openjdk-8-jre-20161012  
FROM benyoo/alpine:jdk-8-20161012  
MAINTAINER from www.dwhd.org by lookback (mondeolove@gmail.com)  
  
ARG MIRROR=http://mirrors.dtops.cc/apache  
ARG VERSION=5.14.2  
LABEL name="ActiveMQ" version=$VERSION  
  
ENV INSTALL_DIR=/data/activemq \  
TEMP_DIR=/tmp/activemq \  
ACTIVEMQ_TCP=61616 \  
ACTIVEMQ_AMQP=5672 \  
ACTIVEMQ_STOMP=61613 \  
ACTIVEMQ_MQTT=1883 \  
ACTIVEMQ_WS=61614 \  
ACTIVEMQ_UI=8161  
RUN set -x && \  
if [[ "$(curl -LI -m 10 -o /dev/null -sw %{http_code} mirrors.ds.com/alpine)"
== "200" ]]; then \  
echo -e
'http://mirrors.ds.com/alpine/v3.4/main\nhttp://mirrors.ds.com/alpine/v3.4/community'
> /etc/apk/repositories; else \  
echo -e 'http://dl-cdn.alpinelinux.org/alpine/v3.4/main\nhttp://dl-
cdn.alpinelinux.org/alpine/v3.4/community' > /etc/apk/repositories; fi && \  
DOWNLOAD=${DOWNLOAD:-$MIRROR/activemq/${VERSION}/apache-
activemq-${VERSION}-bin.tar.gz} && \  
apk --update --no-cache upgrade && \  
apk add --no-cache curl bash tar iproute2 'su-exec>=0.2' && \  
addgroup -g 400 -S activemq && \  
adduser -S -H -G activemq -u 400 -h $INSTALL_DIR -g 'ActiveMQ' activemq && \  
mkdir -p ${INSTALL_DIR} ${TEMP_DIR} && \  
curl -Lk "$DOWNLOAD" | tar xz -C ${INSTALL_DIR} \--strip-components=1 && \  
chown -R activemq:activemq $INSTALL_DIR && \  
apk del curl iptables && \  
rm -rf /var/cache/apk/*  
  
#USER activemq  
ENV PATH=$INSTALL_DIR/bin:$PATH \  
TERM=linux \  
JAVA_HOME=/opt/jdk/jre/bin  
  
WORKDIR $INSTALL_DIR  
EXPOSE $ACTIVEMQ_TCP $ACTIVEMQ_AMQP $ACTIVEMQ_STOMP $ACTIVEMQ_MQTT
$ACTIVEMQ_WS $ACTIVEMQ_UI  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["activemq", "console"]  


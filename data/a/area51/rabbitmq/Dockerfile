FROM area51/alpine  
MAINTAINER Peter Mount <peter@retep.org>  
  
# See README.md for what these mean  
ENV RABBITMQ_VERSION=3.6.9 \  
RABBITMQ_MILESTONE=3.6.9  
ENV RABBITMQ_HOME=/opt/rabbitmq_server-${RABBITMQ_VERSION} \  
PLUGINS_DIR=${RABBITMQ_HOME}/plugins \  
ENABLED_PLUGINS_FILE=${RABBITMQ_HOME}/etc/rabbitmq/enabled_plugins \  
RABBITMQ_MNESIA_BASE=/var/lib/rabbitmq  
  
ENV PATH=$PATH:$RABBITMQ_HOME/sbin  
  
COPY ssl.config ${RABBITMQ_HOME}/etc/rabbitmq/  
COPY standard.config ${RABBITMQ_HOME}/etc/rabbitmq/  
COPY docker-entrypoint.sh /  
  
EXPOSE 5671/tcp 5672/tcp 15672/tcp 15671/tcp  
VOLUME /var/lib/rabbitmq  
ENTRYPOINT ["/docker-entrypoint.sh"]  
#CMD ["/docker-entrypoint.sh"]  
RUN chmod a+x /docker-entrypoint.sh &&\  
apk add --update \  
tar \  
xz \  
bash && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
&& \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add --update-cache --allow-untrusted \  
erlang \  
erlang \  
erlang-mnesia \  
erlang-public-key \  
erlang-crypto \  
erlang-ssl \  
erlang-sasl \  
erlang-asn1 \  
erlang-inets \  
erlang-os-mon \  
erlang-xmerl \  
erlang-eldap \  
erlang-syntax-tools &&\  
cd /opt && \  
milestone=$(echo $RABBITMQ_MILESTONE | tr '.' '_') &&\  
curl -L \  
-o /opt/rmq.tar.xz\  
https://github.com/rabbitmq/rabbitmq-
server/releases/download/rabbitmq_v${milestone}/rabbitmq-server-generic-
unix-${RABBITMQ_VERSION}.tar.xz &&\  
tar -xvf rmq.tar.xz &&\  
rm -f rmq.tar.xz &&\  
touch ${RABBITMQ_HOME}/etc/rabbitmq/enabled_plugins &&\  
rabbitmq-plugins enable \--offline \  
rabbitmq_management \  
rabbitmq_mqtt \  
rabbitmq_shovel \  
rabbitmq_shovel_management \  
rabbitmq_web_stomp &&\  
apk del --purge tar xz &&\  
rm -Rf /var/cache/apk/*  
  
# sed -e "s/# loopback_users.guest = false/loopback_users.guest = false/g" \  
# -i \  
# ${RABBITMQ_HOME}/etc/rabbitmq/rabbitmq.conf  
# ======================================================================  
# The available ports  
# ======================================================================  
# 1883 MQTT  
# 5672 Standard (reserved) AMQP port  
# 15672 Web Management  
# 15674 Web Stomp  
# 25672 Clustering  
# 61613 Stomp  
# ======================================================================  
# EXPOSE 15671 15672 5672 25672 1883 61613  


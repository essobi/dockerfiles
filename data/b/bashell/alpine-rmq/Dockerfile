FROM bashell/alpine-bash:latest  
MAINTAINER Chaiwat Suttipongsakul <cwt@bashell.com>  
  
ENV RABBITMQ_VERSION=3.7.3  
ENV RABBITMQ_SRC=https://dl.bintray.com/rabbitmq/binaries/rabbitmq-server-
generic-unix-$RABBITMQ_VERSION.tar.xz  
ENV RABBITMQ_HOME=/srv/rabbitmq_server-$RABBITMQ_VERSION  
ENV PLUGINS_DIR=$RABBITMQ_HOME/plugins  
ENV ENABLED_PLUGINS_FILE=$RABBITMQ_HOME/etc/rabbitmq/enabled_plugins  
ENV RABBITMQ_MNESIA_BASE=/var/lib/rabbitmq  
  
COPY ssl.config $RABBITMQ_HOME/etc/rabbitmq/  
COPY standard.config $RABBITMQ_HOME/etc/rabbitmq/  
COPY wrapper.sh /usr/bin/wrapper  
RUN chmod a+x /usr/bin/wrapper  
RUN apk add erlang erlang-mnesia erlang-public-key erlang-crypto \  
erlang-ssl erlang-sasl erlang-asn1 erlang-inets erlang-os-mon \  
erlang-xmerl erlang-eldap erlang-sasl erlang-syntax-tools openssl  
RUN apk add xz && cd /srv && \  
wget -q -O - $RABBITMQ_SRC | xz -d - | tar -xf - && \  
touch $RABBITMQ_HOME/etc/rabbitmq/enabled_plugins && \  
$RABBITMQ_HOME/sbin/rabbitmq-plugins enable \--offline rabbitmq_management &&
\  
apk del xz  
  
EXPOSE 5671/tcp 5672/tcp 15672/tcp 15671/tcp  
VOLUME /var/lib/rabbitmq  
CMD ["/usr/bin/wrapper"]  
  


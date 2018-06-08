FROM rafaelpinho/alpine:latest  
  
MAINTAINER Rafael Pinho <rafaelpinho@protonmail.com>  
  
ENV RABBITMQ_VERSION=3.6.1  
  
EXPOSE 5672/tcp \  
15672/tcp  
  
RUN apk add curl \  
tar \  
xz \  
python \  
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
erlang-syntax-tools && \  
  
curl https://www.rabbitmq.com/releases/rabbitmq-
server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-
unix-${RABBITMQ_VERSION}.tar.xz \  
> rabbitmq.tar.xz && \  
  
tar -xvf rabbitmq.tar.xz && \  
  
apk del --purge curl \  
tar \  
xz && \  
  
rm -rf rabbitmq.tar.xz \  
rabbitmq_server-${RABBITMQ_VERSION}/share/ \  
/var/cache/apk \  
/usr/share/man \  
/usr/include \  
/tmp/*  
  
WORKDIR rabbitmq_server-${RABBITMQ_VERSION}  
  
COPY plugins/management-plugin /usr/local/bin/rabbitmqadmin  
  
RUN chmod +x /usr/local/bin/rabbitmqadmin  
  
COPY etc/rabbitmq.config etc/rabbitmq/rabbitmq.config  
  
CMD sbin/rabbitmq-plugins enable --offline rabbitmq_management && \  
sbin/rabbitmq-server  


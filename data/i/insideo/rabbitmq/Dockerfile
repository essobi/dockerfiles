FROM insideo/uc-linux:hydrogen  
MAINTAINER ccondit@randomcoder.com  
  
RUN \  
opkg update && \  
opkg install locale-utils locale-data && \  
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen && \  
opkg remove locale-data locale-utils && \  
export LC_ALL=en_US.UTF-8 && \  
opkg install rabbitmq-server glibc-bin && \  
opkg clean && \  
addgroup -S -g 101 rabbitmq && \  
mkdir -p /var/lib/rabbitmq && \  
adduser -h /var/lib/rabbitmq -g "RabbitMQ user" -s /bin/sh -G rabbitmq -S -D
-u 101 rabbitmq && \  
chown -R rabbitmq:rabbitmq /var/lib/rabbitmq && \  
mkdir -p /etc/rabbitmq && \  
echo "NODENAME=rabbit@localhost" > /etc/rabbitmq/rabbitmq-env.conf && \  
rabbitmq-plugins enable --offline rabbitmq_management && \  
mkdir -p /docker-entrypoint-init.d  
  
COPY docker-entrypoint.sh /  
  
ENV RABBITMQ_LOG_BASE /data/log  
ENV RABBITMQ_MNESIA_BASE /data/mnesia  
ENV LC_ALL en_US.UTF-8  
  
VOLUME /data/log  
VOLUME /data/mnesia  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5672  
EXPOSE 15672  
  
CMD ["rabbitmq-server"]  


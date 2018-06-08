FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y wget && \  
echo "deb http://www.rabbitmq.com/debian/ testing main" | tee
/etc/apt/sources.list.d/rabbitmq.list && \  
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key
add \- && \  
apt-get update && \  
apt-get install -y rabbitmq-server && \  
/usr/sbin/rabbitmq-plugins enable --offline rabbitmq_management
rabbitmq_management_agent rabbitmq_management_visualiser rabbitmq_federation
rabbitmq_federation_management  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN mkdir /opt/rabbit  
ADD run.sh /opt/rabbit/  
  
RUN chmod a+x /opt/rabbit/run.sh  
  
ENV RABBITMQ_LOGS=-  
ENV RABBITMQ_SASL_LOGS=-  
ENV RABBITMQ_CONFIG="[{rabbit, [{loopback_users, []}]}]."  
ENV ERLANG_COOKIE=RABBITMQ  
ENV WAIT_CLUSTERED_WITH="250s"  
VOLUME /var/lib/rabbitmq/mnesia  
  
EXPOSE 5672  
EXPOSE 15672  
EXPOSE 25672  
EXPOSE 4369  
EXPOSE 9100  
EXPOSE 9101  
EXPOSE 9102  
EXPOSE 9103  
EXPOSE 9104  
EXPOSE 9105  
CMD /opt/rabbit/run.sh


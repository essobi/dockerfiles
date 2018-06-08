FROM ubuntu:trusty  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r rabbitmq && useradd -r -d /var/lib/rabbitmq -m -g rabbitmq
rabbitmq  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget python erlang-nox && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
ENV RABBITMQ_VERSION 3.3.5  
ENV RABBITMQ_DEBIAN_VERSION 3.3.5-1  
  
RUN wget -O /tmp/rmq-server.deb http://www.rabbitmq.com/releases/rabbitmq-
server/v${RABBITMQ_VERSION}/rabbitmq-server_${RABBITMQ_DEBIAN_VERSION}_all.deb
\  
&& dpkg -i /tmp/rmq-server.deb \  
&& rm /tmp/rmq-server.deb \  
&& rm -rf /var/lib/apt/lists/*  
# /usr/sbin/rabbitmq-server has some irritating behavior, and only exists to
"su - rabbitmq /usr/lib/rabbitmq/bin/rabbitmq-server ..."  
ENV PATH /usr/lib/rabbitmq/bin:$PATH  
  
RUN echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config  
  
# set home so that any `--user` knows where to put the erlang cookie  
ENV HOME /var/lib/rabbitmq  
  
RUN mkdir -p /var/lib/rabbitmq /etc/rabbitmq \  
&& chown -R rabbitmq:rabbitmq /var/lib/rabbitmq /etc/rabbitmq \  
&& chmod 777 /var/lib/rabbitmq /etc/rabbitmq  
VOLUME /var/lib/rabbitmq  
# add a symlink to the .erlang.cookie in /root so we can "docker exec
rabbitmqctl ..." without gosu  
RUN ln -sf /var/lib/rabbitmq/.erlang.cookie /root/  
  
RUN ln -sf /usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins
/plugins  
# extra utilities to help with local development  
RUN rabbitmq-plugins enable rabbitmq_management  
ADD http://hg.rabbitmq.com/rabbitmq-management/raw-
file/rabbitmq_v3_3_5/bin/rabbitmqadmin /usr/sbin/rabbitmqadmin  
RUN chmod a+x /usr/sbin/rabbitmqadmin  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 4369 5671 5672 25672  
CMD ["rabbitmq-server"]  


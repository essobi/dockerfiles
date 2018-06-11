FROM debian:wheezy  
MAINTAINER Julien Levesy <julien@upfluence.co>  
  
ADD misc/confd /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
ADD http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc
/erlang_solutions.asc  
ADD https://www.rabbitmq.com/rabbitmq-signing-key-public.asc /rabbitmq.asc  
  
RUN echo 'deb http://packages.erlang-solutions.com/debian wheezy contrib' >>
/etc/apt/sources.list && \  
echo 'deb http://www.rabbitmq.com/debian/ testing main' >>
/etc/apt/sources.list && \  
apt-key add erlang_solutions.asc && \  
apt-key add rabbitmq.asc && \  
apt-get update && apt-get -y install erlang rabbitmq-server && \  
apt-get clean  
  
ADD erlang.cookie /var/lib/rabbitmq/.erlang.cookie  
RUN chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie && \  
chmod 400 /var/lib/rabbitmq/.erlang.cookie  
  
ADD conf.d/hosts.toml /etc/confd/conf.d/hosts.toml  
ADD conf.d/rabbitmq.toml /etc/confd/conf.d/rabbitmq.toml  
ADD templates/hosts.tmpl /etc/confd/templates/hosts.tmpl  
ADD templates/rabbitmq.config.tmpl /etc/confd/templates/rabbitmq.config.tmpl  
ADD run.sh /run.sh  
RUN chmod +x /run.sh && \  
mkdir -p /data/mnesia && \  
chown -R rabbitmq:rabbitmq /data/mnesia  
  
EXPOSE 4369  
EXPOSE 25672  
EXPOSE 5672  
ENV RABBITMQ_MNESIA_BASE /data/mnesia  
ENV RABBITMQ_SERVER_START_ARGS -eval error_logger:tty(true).  
  
RUN rabbitmq-plugins --offline enable rabbitmq_management  
  
VOLUME ["/data/mnesia"]  
  
CMD ["/run.sh"]  


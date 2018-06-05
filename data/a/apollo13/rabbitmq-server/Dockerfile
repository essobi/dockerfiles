FROM apollo13/ubuntu:14.04  
MAINTAINER Bohdan Kolecek <kolecek@apollo13.cz>  
  
ENV SERVER_NAME=rabbitmq  
  
RUN \  
# Upgrade Erlang to fix issue with SSL:
http://lists.rabbitmq.com/pipermail/rabbitmq-discuss/2014-May/035963.html  
curl http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc | apt-
key add - && \  
echo "deb http://packages.erlang-solutions.com/ubuntu trusty contrib" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
erlang-nox=1:17.\* \  
erlang-base=1:17.\* \  
erlang-asn1=1:17.\* \  
erlang-corba=1:17.\* \  
erlang-crypto=1:17.\* \  
erlang-diameter=1:17.\* \  
erlang-edoc=1:17.\* \  
erlang-eldap=1:17.\* \  
erlang-erl-docgen=1:17.\* \  
erlang-eunit=1:17.\* \  
erlang-ic=1:17.\* \  
erlang-inets=1:17.\* \  
erlang-inviso=1:17.\* \  
erlang-mnesia=1:17.\* \  
erlang-odbc=1:17.\* \  
erlang-os-mon=1:17.\* \  
erlang-parsetools=1:17.\* \  
erlang-percept=1:17.\* \  
erlang-public-key=1:17.\* \  
erlang-runtime-tools=1:17.\* \  
erlang-snmp=1:17.\* \  
erlang-ssh=1:17.\* \  
erlang-ssl=1:17.\* \  
erlang-syntax-tools=1:17.\* \  
erlang-tools=1:17.\* \  
erlang-webtool=1:17.\* \  
erlang-xmerl=1:17.\* && \  
  
# Install RabbitMQ  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F7B8CEA6056E8E56 && \  
echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y rabbitmq-server pwgen && \  
rabbitmq-plugins enable rabbitmq_management rabbitmq_web_stomp && \  
  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
  
echo "ERLANGCOOKIE" > /var/lib/rabbitmq/.erlang.cookie && \  
chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie && \  
chmod 400 /var/lib/rabbitmq/.erlang.cookie  
  
# Add scripts  
COPY bin/run.sh bin/set_rabbitmq_password.sh /  
  
COPY config/rabbitmq.config /etc/rabbitmq/  
  
EXPOSE 5672 15671 15672 15674  
  
CMD ["/run.sh"]  


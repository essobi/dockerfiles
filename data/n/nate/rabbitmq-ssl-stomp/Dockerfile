FROM ubuntu:14.04  
MAINTAINER Nate Jones <nate@endot.org>  
  
RUN apt-get update && apt-get install -y apt-transport-https wget  
  
# install rabbitmq, which requires a newer erlang package  
RUN echo "deb https://dl.bintray.com/rabbitmq/debian trusty main" >
/etc/apt/sources.list.d/bintray.rabbitmq.list && \  
echo "deb https://packages.erlang-solutions.com/ubuntu trusty contrib" >
/etc/apt/sources.list.d/esl.erlang.list && \  
wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
| apt-key add - && \  
wget -O- wget https://packages.erlang-
solutions.com/ubuntu/erlang_solutions.asc | apt-key add - && \  
apt-get update && \  
apt-get install rabbitmq-server -y  
  
# enable plugins, and restore ownership of the cookie  
RUN rabbitmq-plugins enable rabbitmq_web_stomp rabbitmq_stomp
rabbitmq_management && \  
chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie  
  
RUN apt-get install openssl -y  
ADD ssl /ssl  
  
ADD rabbitmq.config /etc/rabbitmq/rabbitmq.config  
  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
  
# ports are:  
# * SSL AMQP  
# * SSL STOMP  
# * Management  
EXPOSE 5671 61614 15672 5672 61613  
CMD ["/scripts/run.sh"]  


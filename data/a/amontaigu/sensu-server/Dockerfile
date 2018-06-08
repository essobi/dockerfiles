#
================================================================================================================  
#  
# Docker sensu server image  
#  
# @see https://github.com/hiroakis/docker-sensu-server  
# @see https://sensuapp.org/docs/latest/install-sensu  
#
================================================================================================================  
# Base image  
FROM debian:jessie  
  
# Maintainer  
MAINTAINER Alban Montaigu <alban.montaigu@gmail.com>  
  
# Environment configuration  
ENV DEBIAN_FRONTEND="noninteractive"  
# System preparation  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y sudo git wget ruby ruby-dev openssl supervisor build-
essential redis-server \  
&& mkdir -p /var/log/supervisor  
  
# RabbitMQ  
RUN apt-get install -y rabbitmq-server \  
&& git clone git://github.com/joemiller/joemiller.me-intro-to-sensu.git \  
&& cd joemiller.me-intro-to-sensu \  
&& ./ssl_certs.sh clean \  
&& ./ssl_certs.sh generate \  
&& mkdir /etc/rabbitmq/ssl \  
&& cp /joemiller.me-intro-to-sensu/server_cert.pem /etc/rabbitmq/ssl/cert.pem
\  
&& cp /joemiller.me-intro-to-sensu/server_key.pem /etc/rabbitmq/ssl/key.pem \  
&& cp /joemiller.me-intro-to-sensu/testca/cacert.pem /etc/rabbitmq/ssl/  
ADD ./sensu/rabbitmq.config /etc/rabbitmq/  
RUN rabbitmq-plugins enable rabbitmq_management  
  
# Sensu server  
RUN wget -q http://repositories.sensuapp.org/apt/pubkey.gpg -O- | sudo apt-key
add - \  
&& echo "deb http://repositories.sensuapp.org/apt sensu main" | sudo tee
/etc/apt/sources.list.d/sensu.list \  
&& apt-get update \  
&& apt-get install -y sensu  
ADD ./sensu/config.json /etc/sensu/  
RUN mkdir -p /etc/sensu/ssl \  
&& cp /joemiller.me-intro-to-sensu/client_cert.pem /etc/sensu/ssl/cert.pem \  
&& cp /joemiller.me-intro-to-sensu/client_key.pem /etc/sensu/ssl/key.pem \  
&& gem install sensu-plugin \  
&& gem install sensu-plugins-mailer  
  
# uchiwa  
RUN apt-get install -y uchiwa \  
&& rm -r /var/lib/apt/lists/*  
ADD ./sensu/uchiwa.json /etc/sensu/  
  
# supervisord  
ADD ./supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 3000 4567 5671 15672  
# Main process  
CMD ["/usr/bin/supervisord"]  


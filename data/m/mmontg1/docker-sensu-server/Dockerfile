FROM centos:centos6  
  
MAINTAINER Hiroaki Sano <hiroaki.sano.9stories@gmail.com>  
  
# Basic packages  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm \  
&& yum -y install passwd sudo git wget openssl openssh openssh-server openssh-
clients gcc-c++  
  
# Create user  
RUN useradd hiroakis \  
&& echo "hiroakis" | passwd hiroakis --stdin \  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config \  
&& echo "hiroakis ALL=(ALL) ALL" >> /etc/sudoers.d/hiroakis  
  
# Redis  
RUN yum install -y redis  
  
# RabbitMQ  
RUN yum install -y erlang \  
&& rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc \  
&& rpm -Uvh http://www.rabbitmq.com/releases/rabbitmq-server/v3.1.4/rabbitmq-
server-3.1.4-1.noarch.rpm \  
&& git clone git://github.com/joemiller/joemiller.me-intro-to-sensu.git \  
&& cd joemiller.me-intro-to-sensu/; ./ssl_certs.sh clean && ./ssl_certs.sh
generate \  
&& mkdir /etc/rabbitmq/ssl \  
&& cp /joemiller.me-intro-to-sensu/server_cert.pem /etc/rabbitmq/ssl/cert.pem
\  
&& cp /joemiller.me-intro-to-sensu/server_key.pem /etc/rabbitmq/ssl/key.pem \  
&& cp /joemiller.me-intro-to-sensu/testca/cacert.pem /etc/rabbitmq/ssl/  
ADD ./files/rabbitmq/rabbitmq.config /etc/rabbitmq/  
RUN rabbitmq-plugins enable rabbitmq_management  
  
# Sensu server  
ADD ./files/sensu/sensu.repo /etc/yum.repos.d/  
RUN yum install -y sensu  
ADD ./files/sensu/config.json /etc/sensu/  
RUN mkdir -p /etc/sensu/ssl \  
&& cp /joemiller.me-intro-to-sensu/client_cert.pem /etc/sensu/ssl/cert.pem \  
&& cp /joemiller.me-intro-to-sensu/client_key.pem /etc/sensu/ssl/key.pem \  
&& echo 'LOG_LEVEL=debug' >> /etc/default/sensu  
COPY ./files/sensu/checks/* /etc/sensu/plugins/  
COPY ./files/sensu/definitions/* /etc/sensu/conf.d/  
COPY ./files/sensu/handlers/* /etc/sensu/conf.d/  
COPY ./files/sensu/influxdb.json /etc/sensu/conf.d/influxdb.json  
RUN mkdir /opt/sensu/.gem && chown sensu:sensu /opt/sensu/.gem && chown -R
sensu:sensu /opt/sensu  
RUN su -c "/opt/sensu/embedded/bin/gem install --user-install em-http-request
influxdb multi_json" -s /bin/sh sensu  
RUN wget -O /etc/sensu/extensions/influxdb.rb
https://raw.githubusercontent.com/naemono/sensu-influxdb-
extension/master/influxdb.rb  
  
# uchiwa  
RUN yum install -y uchiwa  
ADD ./files/sensu/uchiwa.json /etc/sensu/  
  
# supervisord  
RUN wget http://peak.telecommunity.com/dist/ez_setup.py;python ez_setup.py \  
&& easy_install supervisor  
ADD files/supervisord.conf /etc/supervisord.conf  
  
RUN /etc/init.d/sshd start && /etc/init.d/sshd stop  
  
EXPOSE 22 3000 4567 5671 15672  
CMD ["/usr/bin/supervisord"]  


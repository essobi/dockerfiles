FROM ubuntu:14.04  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
VOLUME ["/var/lib/rabbitmq"]  
  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
COPY ./rabbitmq-server-wrapper.sh /usr/sbin/rabbitmq-server-wrapper  
ADD http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
/tmp/erlang-solutions-repo.deb  
ADD https://github.com/rabbitmq/rabbitmq-
server/releases/download/rabbitmq_v3_5_3/rabbitmq-server_3.5.3-1_all.deb
/tmp/rabbitmq-server.deb  
  
RUN dpkg -i /tmp/erlang-solutions-repo.deb 2> /dev/null \  
&& apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get install -y erlang-base erlang-nox > /dev/null \  
&& dpkg -i /tmp/rabbitmq-server.deb > /dev/null \  
&& apt-get clean > /dev/null \  
&& rm /tmp/*.deb \  
&& chown -R rabbitmq:rabbitmq /var/lib/rabbitmq  
  
USER root  
EXPOSE 5672  
CMD ["/usr/sbin/rabbitmq-server-wrapper"]  


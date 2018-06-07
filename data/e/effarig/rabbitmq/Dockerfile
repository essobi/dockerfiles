FROM effarig/archlinux  
  
MAINTAINER docker@effarig.co.uk  
  
RUN pacman --noconfirm -Suy && \  
pacman --noconfirm -S erlang-nox  
  
ADD https://www.rabbitmq.com/releases/rabbitmq-server/v3.4.2/rabbitmq-server-
generic-unix-3.4.2.tar.gz /opt/rabbitmq.tar.gz  
  
RUN cd /opt \  
&& tar xzf rabbitmq.tar.gz \  
&& rm rabbitmq.tar.gz \  
&& mv rabbitmq_server-* rabbitmq \  
&& useradd -r -s /usr/bin/nologin rabbitmq \  
&& mkdir -p /run/rabbitmq /opt/rabbitmq/etc/rabbitmq
/volumes/{mnesia,logs,home} \  
&& chown rabbitmq:rabbitmq /run/rabbitmq /volumes/{mnesia,logs,home}  
  
USER rabbitmq  
  
VOLUME [ "/volumes/mnesia", "/volumes/logs", "/volumes/home" ]  
  
# Ports:  
# 4369 (epmd)  
# 25672 (Erlang distribution)  
# 5672, 5671 (AMQP 0-9-1 without and with TLS)  
# 15672 (if management plugin is enabled)  
# 61613, 61614 (if STOMP is enabled)  
# 1883, 8883 (if MQTT is enabled)  
  
EXPOSE 4369 25672 5672 5671 15672 61613 61614 1883 8883  
  
ENV RABBITMQ_MNESIA_DIR /volumes/mnesia  
ENV RABBITMQ_LOGS /volumes/logs/rabbit.log  
ENV RABBITMQ_SASL_LOGS /volumes/logs/sasl.log  
ENV RABBITMQ_PID_FILE /run/rabbitmq/rabbitmq.pid  
ENV RABBITMQ_PLUGINS_EXPAND_DIR /volumes/mnesia/plugins-expand  
ENV HOME /volumes/home  
  
ENTRYPOINT [ "/opt/rabbitmq/sbin/rabbitmq-server" ]  
  
  
############################################################################  
# To run with insecure test user (password test) with access to everything  
# from anywhere.  
############################################################################  
# docker run -ti --rm --name=rabbit -p 127.0.0.1:5672:5672 \--hostname=rabbit
effarig/rabbitmq  
# docker exec -ti rabbit bash  
# ./rabbitmqctl add_user test test  
# ./rabbitmqctl set_permissions -p / test ".*" ".*" ".*"  
############################################################################  


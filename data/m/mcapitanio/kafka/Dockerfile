FROM mcapitanio/centos-java  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.it>  
  
USER root  
  
ENV CONFLUENT_PLATFORM_VER 3.2  
ENV KAFKA_TOPICS_UI_VER 0.8.3  
# Install Confluent Repo  
RUN rpm --import
http://packages.confluent.io/rpm/${CONFLUENT_PLATFORM_VER}/archive.key  
COPY confluent.repo /etc/yum.repos.d/  
  
# Install needed packages  
RUN yum install -y deltarpm  
RUN yum clean all; yum update -y  
RUN yum install -y git \  
python-pip \  
python-setuptools \  
wget \  
unzip  
RUN easy_install supervisor  
RUN yum clean all  
  
WORKDIR /opt/docker  
  
# All Kafka Stuff  
RUN yum install -y confluent-kafka-2.11  
RUN yum install -y confluent-kafka-rest  
RUN yum install -y confluent-schema-registry  
  
# Kafka Topics UI  
RUN wget "https://caddyserver.com/download/linux/amd64" -O caddy.tgz; \  
mkdir /opt/caddy; \  
tar xzf caddy.tgz -C /opt/caddy; \  
rm -f caddy.tgz  
  
# Add and Setup Kafka-Topics-Ui  
RUN wget https://github.com/Landoop/kafka-topics-
ui/releases/download/v${KAFKA_TOPICS_UI_VER}/kafka-topics-
ui-${KAFKA_TOPICS_UI_VER}.tar.gz -O kafka-topics-ui.tar.gz; \  
mkdir /opt/kafka-topics-ui; \  
tar xzf kafka-topics-ui.tar.gz -C /opt/kafka-topics-ui; \  
rm -f kafka-topics-ui.tar.gz  
  
COPY *.sh ./  
ADD kafka-topics-ui/Caddyfile /opt/caddy/  
ADD kafka-topics-ui/run.sh /opt/kafka-topics-ui/  
RUN chmod +x supervisord-bootstrap.sh  
  
COPY etc/ /etc/  
  
EXPOSE 9092 8081 8082 8083  
VOLUME [ "/etc/kafka", "/var/log/kafka", "/etc/kafka-rest", "/etc/schema-
registry" ]  
  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  


#
# Kafka Dockerfile
#
FROM ubuntu:vivid

# set env
ENV DEBIAN_FRONTEND noninteractive

# set apt-get repository
ARG APT_MIRROR=jp.archive.ubuntu.com
RUN sed -i "s/archive.ubuntu.com/${APT_MIRROR}/g" /etc/apt/sources.list

# Setting Environment
ENV VERSION 0.8.2.2
# install dependencies
RUN apt-get update; apt-get install -y unzip openjdk-6-jdk wget git libsnappy-dev

RUN wget -q http://ftp.riken.jp/net/apache/kafka/${VERSION}/kafka_2.10-${VERSION}.tgz -O /tmp/kafka_2.10-${VERSION}.tgz
RUN tar xfz /tmp/kafka_2.10-${VERSION}.tgz -C /opt
RUN mv /opt/kafka_2.10-${VERSION} /opt/kafka
ENV KAFKA_HOME /opt/kafka

# Expose ports
EXPOSE 9092
WORKDIR /opt/kafka

# run kafka
CMD bin/kafka-server-start.sh config/server.properties

#Cleanup
RUN rm -rf /tmp/*

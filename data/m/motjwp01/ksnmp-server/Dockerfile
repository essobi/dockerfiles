FROM ubuntu:artful  
  
MAINTAINER Jason W. Plummer "vhsjwp01@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TERM vt100  
  
ENV DATA_DIR /data  
ENV KAFKA_DATA_DIR ${DATA_DIR}/kafka  
ENV ZK_DATA_DIR ${DATA_DIR}/zookeeper  
  
ENV KAFKA_LOG_DIR ${DATA_DIR}/logs/kafka  
ENV KAFKA_REST_LOG_DIR ${DATA_DIR}/logs/kafka-rest  
ENV SNMP_PERFMON_LOG_DIR ${DATA_DIR}/logs/snmp-perfmon  
ENV SNMPD_LOG_DIR ${DATA_DIR}/logs/snmpd  
ENV SNMPTRAP_LOG_DIR ${DATA_DIR}/logs/snmp  
ENV SNMPTRAPD_LOG_DIR ${DATA_DIR}/logs/snmptrapd  
ENV SYSLOG_NG_LOG_DIR ${DATA_DIR}/logs/syslog-ng  
ENV ZK_LOG_DIR ${DATA_DIR}/logs/zookeeper  
  
ENV KAFKA_LOG_FILE kafka_runtime.log  
ENV KAFKA_REST_LOG_FILE kafka-rest_runtime.log  
ENV SNMP_PERFMON_LOG_FILE snmp-perfmon_runtime.log  
ENV SNMPD_LOG_FILE snmpd_runtime.log  
ENV SNMPTRAP_JSON_FILE snmptrapd_json.log  
ENV SNMPTRAP_LOG_FILE snmptrapd.log  
ENV SNMPTRAPD_LOG_FILE snmptrapd_runtime.log  
ENV SYSLOG_NG_LOG_FILE syslog-ng_runtime.log  
ENV ZK_LOG_FILE zookeeper_runtime.log  
  
ENV KAFKA_BROKER_ID 0  
ENV KAFKA_ZK_CONNECT localhost:2181/SNMP  
  
ENV SYSLOG_NG_KAFKA_CONNECT localhost:9092  
ENV SYSLOG_NG_KAFKA_TOPIC SNMP  
  
# Get the base tools installed  
RUN apt-get update -y && \  
apt-get --allow-unauthenticated -o Dpkg::Options::="--force-confold" install
-y \  
apt-file bc curl elinks gnupg htop iftop iotop jq libterm-readline-gnu-perl \  
lm-sensors make net-tools openjdk-8-jre-headless perl-doc runit-init snmp \  
snmp-mibs-downloader snmpd snmptrapd software-properties-common unzip vim wget
&& \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y && \  
apt-file update  
  
# Install the latest deb source for syslog-ng  
RUN wget -qO -
http://download.opensuse.org/repositories/home:/laszlo_budai:/syslog-
ng/xUbuntu_17.04/Release.key \  
| apt-key add - && \  
echo "deb
http://download.opensuse.org/repositories/home:/laszlo_budai:/syslog-
ng/xUbuntu_17.04 ./" > \  
/etc/apt/sources.list.d/syslog-ng-obs.list && \  
apt-get update -y && \  
apt-get install syslog-ng-core syslog-ng-mod-json syslog-ng-mod-kafka syslog-
ng-mod-snmptrapd-parser -y  
  
# Install Confluent REST API for Kafka  
# NOTE: Confluent provides an apt repo for installing their software  
RUN wget -qO - http://packages.confluent.io/deb/3.3/archive.key | apt-key add
- && \  
add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.3
stable main" && \  
apt-get update && \  
apt-get install -y confluent-platform-oss-2.11  
  
# Install ZooKeeper  
# NOTE: ubuntu v17 has packaged versions of zookeeper  
RUN apt-get install -y zookeeper zookeeper-bin zookeeperd  
  
# Install Kafka  
# NOTE: This block figures out the nearest apache mirror, then figures out the  
# latest version of kafka, then figures out the latest version of scala  
# that goes with it. It then downloads the archive, unpacks it, then removes  
# the archive for housekeeping  
RUN mirror=$(curl --stderr /dev/null
https://www.apache.org/dyn/closer.cgi\?as_json\=1 | \  
jq -r '.preferred') && \  
latest_kafka=$(elinks -verbose 1 -dump 1 "${mirror}kafka/?C=M;O=A" | \  
egrep "${mirror}kafka/" | awk '{print $NF}' | tail -1) && \  
url=$(elinks -verbose 1 -dump 1 "${latest_kafka}?C=M;O=A" | \  
egrep "${latest_kafka}kafka_.*\\.tgz$" | awk '{print $NF}' | tail -1) && \  
local_archive=$(echo "${url}" | awk -F'/' '{print $NF}') && \  
local_dirname=$(echo "${local_archive}" | sed -e 's/\\.tgz$//g') && \  
wget -q "${url}" -O "/tmp/${local_archive}" && \  
tar xf "/tmp/${local_archive}" -C /opt && \  
ln -s "/opt/${local_dirname}" "/opt/kafka-latest" && \  
rm -rf "/tmp/${local_archive}"  
  
# Make base data and log directories  
RUN if [ ! -d /data ]; then \  
mkdir -p /data ; \  
fi && \  
if [ ! -d /data/logs ]; then \  
mkdir -p /data/logs ; \  
fi  
  
# Configure ZooKeeper for standalone operations  
COPY files/zookeeper/etc/zookeeper/conf/zoo.cfg /etc/zookeeper/conf/  
RUN chmod 644 /etc/zookeeper/conf/zoo.cfg  
  
# Configure Kafka for standalone operations  
COPY files/kafka/opt/kafka-latest/config/server.properties /opt/kafka-
latest/config/  
RUN chmod 644 /opt/kafka-latest/config/server.properties  
RUN rm -rf /opt/kafka-latest/logs && \  
ln -s "${KAFKA_LOG_DIR}" /opt/kafka-latest/logs  
  
# Configure Confluent Kafka-REST for standalone operations  
COPY files/kafka-rest/etc/kafka-rest/kafka-rest.properties /etc/kafka-rest/  
RUN chmod 644 /etc/kafka-rest/kafka-rest.properties  
  
# Configure SNMP for standalone operations  
COPY files/snmp/etc/snmp/* /etc/snmp/  
COPY files/snmp/etc/default/* /etc/default/  
COPY files/snmp_perfmon/usr/local/sbin/* /usr/local/sbin  
  
# Configure syslog-ng for standalone operations  
COPY files/syslog-ng/etc/syslog-ng/* /etc/syslog-ng/  
  
# Configure runit for service choreography  
RUN rm -rf /etc/service/* && \  
for run_dir in 10-zookeeper 20-kafka 30-snmptrapd 40-snmpd 50-syslog-ng
60-kafka-rest 70-snmp_perfmon ; do \  
mkdir -p "/etc/service/${run_dir}" ; \  
done  
COPY files/runit/etc/service/10-zookeeper/* /etc/service/10-zookeeper/  
COPY files/runit/etc/service/20-kafka/* /etc/service/20-kafka/  
COPY files/runit/etc/service/30-snmptrapd/* /etc/service/30-snmptrapd/  
COPY files/runit/etc/service/40-snmpd/* /etc/service/40-snmpd/  
COPY files/runit/etc/service/50-syslog-ng/* /etc/service/50-syslog-ng/  
COPY files/runit/etc/service/60-kafka-rest/* /etc/service/60-kafka-rest/  
COPY files/runit/etc/service/70-snmp_perfmon/* /etc/service/70-snmp_perfmon/  
  
EXPOSE 8082  
ENTRYPOINT /usr/bin/runsvdir /etc/service  


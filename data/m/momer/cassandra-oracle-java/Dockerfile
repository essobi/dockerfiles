# Dockerfile for Cassandra  
FROM momer/maestro-base-oracle-jdk:0.0.2  
# Credit goes to Original Source & actual Maintainer  
# MAINTAINER Maxime Petazzoni <max@signalfuse.com>  
MAINTAINER Mo Omer <momer@cmithun.com>  
  
# I only added:  
# - Docker base which uses Oracle Java 7  
# - Update to Cassandra 2.0.9  
# - Exposed ports for cassandra & its tools  
# - Use docker container internal_address for all of  
# - internal_address  
# - rpc_address  
# - seed  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Python YAML is needed to tweak Cassandra's configuration  
RUN apt-get update  
RUN apt-get -y install python-yaml cron supervisor  
  
# supervisord  
RUN mkdir -p /var/log/supervisor/cassandra  
  
# Get the latest stable version of Cassandra  
RUN wget -q -O - http://archive.apache.org/dist/cassandra/2.0.9/apache-
cassandra-2.0.9-bin.tar.gz \  
| tar -C /opt -xz  
  
ADD jmxagent.jar /opt/apache-cassandra-2.0.9/lib/  
ADD run.py /opt/apache-cassandra-2.0.9/.docker/  
ADD supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Cron job to repair cassandra  
RUN mkdir -p /var/lib/.docker  
ADD ./install /  
RUN chmod +x /var/lib/.docker/cassandra_cron.conf  
  
RUN /bin/bash -c "/usr/bin/crontab /var/lib/.docker/cassandra_cron.conf"  
  
WORKDIR /opt/apache-cassandra-2.0.9  
VOLUME /var/lib/cassandra/saved_caches  
VOLUME /var/lib/cassandra/data  
VOLUME /var/lib/cassandra/commitlog  
VOLUME /var/log/cassandra  
VOLUME /var/log/supervisor  
  
EXPOSE 9160 9042 7199 7001 7000 4243  
  
CMD ["python", "/opt/apache-cassandra-2.0.9/.docker/run.py"]  


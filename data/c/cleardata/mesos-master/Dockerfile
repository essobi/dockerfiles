FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV MESOS_IP 0.0.0.0  
ENV MESOS_LOG_DIR /var/log/mesos/  
ENV MESOS_WORK_DIR /var/lib/mesos/  
ENV MESOS_QUORUM 1  
RUN apt-get update -y && apt-get install -y software-properties-common python-
software-properties && apt-key adv --keyserver keyserver.ubuntu.com --recv
E56151BF && echo "deb http://repos.mesosphere.io/ubuntu trusty main" >
/etc/apt/sources.list.d/mesosphere.list && apt-get update -y && apt-get
install -y --no-install-recommends openjdk-6-jre-headless mesos && rm -rf
/var/lib/apt/lists/*  
EXPOSE 5050  
VOLUME ["/var/log/mesos/", "/var/lib/mesos/"]  
ENTRYPOINT ["/usr/sbin/mesos-master"]  


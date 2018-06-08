FROM java:8-jdk  
  
ARG MESOS_VERSION=1.0.1-2.0.93.debian81  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y apt-transport-https ca-certificates
curl  
  
RUN echo "deb http://repos.mesosphere.com/debian jessie main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
apt-get -y update && \  
apt-get -y install curl mesos=${MESOS_VERSION} && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN curl -fLsS https://get.docker.com/ | sh && test -x /usr/bin/docker  
  
ENV MESOS_WORK_DIR /tmp/mesos  
ENV MESOS_LOG_DIR /var/log/mesos  
ENV MESOS_CONTAINERIZERS docker,mesos  
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/local/lib/libmesos.so  
  
# https://mesosphere.github.io/marathon/docs/native-docker.html  
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins  
  
# https://issues.apache.org/jira/browse/MESOS-4675  
ENV MESOS_SYSTEMD_ENABLE_SUPPORT false  
  
VOLUME /tmp/mesos  
  
VOLUME /var/log/mesos  


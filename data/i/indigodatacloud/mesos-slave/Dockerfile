FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get install -y apt-transport-https  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo deb http://repos.mesosphere.io/ubuntu trusty main >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get update && \  
apt-get -y install mesos  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo deb https://apt.dockerproject.org/repo ubuntu-trusty main >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -y docker-engine && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["/usr/sbin/mesos-slave"]  
  
ENV MESOS_WORK_DIR /tmp/mesos  
ENV MESOS_CONTAINERIZERS docker,mesos  
  
# https://mesosphere.github.io/marathon/docs/native-docker.html  
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins  
  
VOLUME /tmp/mesos  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  


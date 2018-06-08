# Docker file for mesos slave container, normally no modification required.  
FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y curl  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo deb http://repos.mesosphere.io/ubuntu trusty main >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get update && \  
apt-get -y install mesos=0.24.1-0.2.35.ubuntu1404 wget  
  
# http://docs.docker.com/installation/ubuntulinux/  
RUN wget -O /usr/bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-1.10.0&&chmod +x
/usr/bin/docker  
  
CMD ["/usr/sbin/mesos-slave"]  
  
ENV MESOS_WORK_DIR /tmp/mesos  
ENV MESOS_CONTAINERIZERS docker,mesos  
  
# https://mesosphere.github.io/marathon/docs/native-docker.html  
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins  
  
VOLUME /tmp/mesos  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  


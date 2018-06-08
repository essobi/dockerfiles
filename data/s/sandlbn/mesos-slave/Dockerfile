FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y curl  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo deb http://repos.mesosphere.io/ubuntu trusty main >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get update && \  
apt-get -y install mesos=0.27.1-2.0.226.ubuntu1404  
  
# http://docs.docker.com/installation/ubuntulinux/  
RUN curl -fLsS https://get.docker.com/ | sh  
  
CMD ["/usr/sbin/mesos-slave"]  
  
ENV MESOS_WORK_DIR /tmp/mesos  
ENV MESOS_CONTAINERIZERS docker,mesos  
  
# https://mesosphere.github.io/marathon/docs/native-docker.html  
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins  
  
# https://issues.apache.org/jira/browse/MESOS-3793  
ENV MESOS_LAUNCHER posix  
  
VOLUME /tmp/mesos  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  


FROM registry.cn-hangzhou.aliyuncs.com/rainbow954/mesos:latest  
  
#Docker  
RUN apt-get update && apt-get install -y curl apt-transport-https ca-
certificates lxc iptables apparmor && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo deb https://apt.dockerproject.org/repo ubuntu-xenial main >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get -y install docker-engine  
  
CMD ["/usr/sbin/mesos-slave"]  
  
ENV MESOS_WORK_DIR /tmp/mesos  
ENV MESOS_CONTAINERIZERS docker,mesos  
  
# https://mesosphere.github.io/marathon/docs/native-docker.html  
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins  
  
# https://issues.apache.org/jira/browse/MESOS-4675  
ENV MESOS_SYSTEMD_ENABLE_SUPPORT false  
  
VOLUME /tmp/mesos  
  
COPY entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]


FROM ubuntu:trusty  
MAINTAINER Stanley Yeo <yyoud88@gmail.com>  
WORKDIR /opt  
RUN apt-get update && apt-get install -qqy openjdk-7-jre-headless curl && \  
curl -sSfL
http://downloads.mesosphere.io/master/ubuntu/14.04/mesos_0.19.1-1.0.ubuntu1404_amd64.deb
--output mesos.deb && \  
dpkg -i mesos.deb && \  
apt-get -f -y install && \  
rm mesos.deb && \  
curl -sSfL
http://downloads.mesosphere.io/chronos/chronos-2.1.0_mesos-0.14.0-rc4.tgz
--output chronos.tgz && \  
tar xzf chronos.tgz && \  
rm chronos.tgz  
EXPOSE 4400  
CMD /opt/chronos/bin/start-chronos.bash \--master $MASTER \--zk_hosts
$ZK_HOSTS \--http_port 4400


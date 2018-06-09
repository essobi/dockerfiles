FROM baselibrary/java:8  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV MESOS_MAJOR 0.25  
ENV MESOS_RELEASE 0.25.0-0.2.70.ubuntu1404  
  
## Repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E56151BF &&\  
echo "deb http://repos.mesosphere.com/ubuntu trusty main" >
/etc/apt/sources.list.d/mesosphere.list  
  
## Packages  
RUN \  
apt-get update &&\  
apt-get install -y mesos=$MESOS_RELEASE iptables libapparmor1 &&\  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/var/lib/mesos"]  
  
CMD ["mesos"]  
  


FROM ottoops/mesos-java7:latest  
MAINTAINER "Paul Otto" <paul@ottoops.com>  
  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get update -y && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
apt-get install -y maven supervisor apt-transport-https && \  
echo "deb https://get.docker.com/ubuntu docker main" >
/etc/apt/sources.list.d/docker.list && \  
apt-get update -y && \  
apt-get install -y lxc-docker-1.3.3 && \  
mkdir -p /var/log/supervisor  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  


FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && \  
apt-get install -y --no-install-recommends apt-transport-https ca-certificates
software-properties-common  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >
/etc/apt/sources.list.d/docker.list && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
add-apt-repository ppa:openjdk-r/ppa -y && \  
apt-get update -qq  
  
RUN apt-get install -y --no-install-recommends \  
curl \  
lxc \  
iptables \  
openjdk-8-jdk \  
wget \  
unzip \  
docker-engine=1.12.0-0~trusty \  
git \  
gitstats  
  
ADD wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
VOLUME /var/lib/docker  
  
RUN groupadd -g 1000 jenkins && \  
useradd -d /home/jenkins -s /bin/bash -m jenkins -u 1000 -g jenkins && \  
usermod -a -G docker jenkins  
  
RUN wget -O /home/jenkins/swarm-client.jar http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-client/3.3/swarm-client-3.3.jar  
  
ADD jenkins-slave-run.sh /  
CMD ["/jenkins-slave-run.sh"]  


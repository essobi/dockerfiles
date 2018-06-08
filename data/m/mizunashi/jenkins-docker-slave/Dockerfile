FROM mizunashi/jenkins-swarm-slave  
MAINTAINER Mizunashi Mana <mizunashi_mana@mma.club.uec.ac.jp>  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https ca-certificates \  
curl lxc iptables supervisor  
  
RUN curl -sSL https://get.docker.com/ubuntu/ | sh  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
COPY install.sh /var/cache/jenkins-docker-slave/install.sh  
RUN bash /var/cache/jenkins-docker-slave/install.sh  
  
VOLUME ["/var/lib/docker"]  
  
# from jenkins-slave image  
RUN usermod -a -G docker ${JENKINS_WORKUSER}  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  


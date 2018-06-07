FROM ubuntu:14.04  
MAINTAINER Decheng Zhang <killercentury@gmail.com>  
  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
ENV DOCKER_COMPOSE_VERSION 1.3.3  
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
RUN apt-get update && apt-get install -y zip supervisor jenkins && rm -rf
/var/lib/apt/lists/*  
ENV JENKINS_HOME /var/lib/jenkins  
VOLUME /var/lib/jenkins  
  
# Install Docker Compose  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
ADD ./initgroup /usr/local/bin/initgroup  
RUN chmod +x /usr/local/bin/initgroup  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 8080  
CMD ["/usr/bin/supervisord"]


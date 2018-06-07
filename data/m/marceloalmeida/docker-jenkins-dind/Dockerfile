FROM debian:jessie-backports  
  
MAINTAINER Marcelo Almeida <ms.almeida86@gmail.com>  
  
ENV \  
DEBIAN_FRONTEND="noninteractive" \  
JENKINS_VERSION="2.62"  
# Let's start with some basic stuff.  
RUN apt-get update && apt-get -t jessie-backports install -y --no-install-
recommends \  
apt-transport-https \  
ca-certificates \  
ca-certificates-java \  
curl \  
lxc \  
iptables \  
git \  
zip \  
supervisor \  
openjdk-8-jre-headless \  
daemon \  
net-tools \  
ssh \  
psmisc && \  
curl -s -L -O http://pkg.jenkins-
ci.org/debian/binary/jenkins_${JENKINS_VERSION}_all.deb && \  
dpkg -i jenkins_${JENKINS_VERSION}_all.deb && \  
rm -f jenkins_${JENKINS_VERSION}_all.deb && \  
# CLEANUP  
apt-get autoremove -yq --purge && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install the wrapper script from
https://raw.githubusercontent.com/docker/docker/master/hack/dind.  
ADD https://raw.githubusercontent.com/docker/docker/master/hack/dind
/usr/local/bin/dind  
RUN chmod +x /usr/local/bin/dind  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
ENV \  
JENKINS_HOME="/var/lib/jenkins" \  
GIT_TIMEOUT="60" \  
MAX_HEAP_SIZE="512m" \  
MAX_PERM_SIZE="2048m"  
RUN \  
usermod -a -G docker jenkins  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 8080  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


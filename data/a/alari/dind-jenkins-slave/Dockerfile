# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM dockerfile/java:openjdk-7-jdk  
  
# Make sure the package repository is up to date.  
RUN apt-get update -qq  
  
RUN mkdir -p /var/run/sshd  
  
RUN apt-get install -qqy apt-transport-https  
  
# Install Docker from Docker Inc. repositories  
RUN echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9  
RUN apt-get update -qq && \  
apt-get install -y apparmor ca-certificates iptables lxc-docker openssh-server
&& \  
apt-get clean  
  
RUN adduser --quiet jenkins  
  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
VOLUME /var/lib/docker  
  
# Make sure that the "jenkins" user from evarga's image is part of the
"docker"  
# group. Needed to access the docker daemon's unix socket.  
RUN usermod -a -G docker jenkins  
  
# place the jenkins slave startup script into the container  
ADD jenkins-slave-startup.sh /  
RUN chmod +x /jenkins-slave-startup.sh  
CMD ["/jenkins-slave-startup.sh"]  
  
ENV PORT 2375  


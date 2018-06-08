#### credit to evarga/jenkins-slave and tehranian/dind-jenkins-slave  
# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM buildpack-deps:wheezy-scm  
MAINTAINER Brandon Mangold <bmangold@docker.com>  
  
ENV REFRESHED_AT 2015-04-15  
EXPOSE 22  
ENTRYPOINT ["/docker-entrypoint.sh"]  
WORKDIR /home/jenkins  
VOLUME /var/lib/docker  
  
# Install some dependencies, and docker  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables \  
openssh-server \  
openjdk-7-jdk \  
&& curl -sSL https://test.docker.com/ubuntu/ -o install-docker.sh \  
&& [ $( shasum install-docker.sh | cut -d ' ' -f 1 ) =
"fb5ff1718d5b66642e1638f21eaf63f4faa2e9a6" ] \  
&& sh install-docker.sh \  
&& apt-get -y upgrade \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add user jenkins in groups: jenkins,docker and give it sudo permissions  
RUN adduser --quiet jenkins \  
&& usermod -a -G docker jenkins \  
&& echo "jenkins:jenkins" | chpasswd \  
&& echo "jenkins ALL= NOPASSWD: ALL" >> /etc/sudoers \  
&& mkdir -p /home/jenkins  
  
# install docker-in-docker  
RUN mkdir -p /usr/app/dind/ \  
&& curl -sSL
https://github.com/jpetazzo/dind/archive/ed31b17f8688806d16c79505e7c02c47317b280b.tar.gz
-o "dind.tar.gz" \  
&& [ $( shasum dind.tar.gz | cut -d ' ' -f 1 ) =
"80959b34181366552acb5886952627e53f138361" ] \  
&& tar -xzf dind.tar.gz -C /usr/app/dind/ --strip-components=1 \  
&& ln -nfs /usr/app/dind/wrapdocker /usr/local/bin/wrapdocker  
  
# Configure SSHd  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd \  
&& mkdir -p /var/run/sshd  
  
# place the jenkins slave startup script into the container  
COPY docker-entrypoint.sh /  


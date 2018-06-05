# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM ubuntu:16.04  
MAINTAINER Tobias Olsson <tobias@olsson.be>  
  
# In case you need proxy  
#RUN echo 'Acquire::http::Proxy "http://127.0.0.1:8080";' >> /etc/apt/apt.conf  
  
# Add locales after locale-gen as needed  
# Upgrade packages on image  
# Preparations for sshd  
run apt-get -q update &&\  
apt-get install -y \--no-install-recommends locales &&\  
locale-gen en_US.UTF-8 &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server wget software-
properties-common &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
  
# Install Oracle JDK 8 (latest stable edition)  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN add-apt-repository ppa:webupd8team/java && apt-get update && apt-get clean
&& apt-get install -y oracle-java8-installer && apt-get install --no-install-
recommends -y git mercurial subversion oracle-java8-set-default groovy2 && rm
-f /var/cache/apt/*.bin  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
  
# Default command  
CMD ["/usr/sbin/sshd", "-D"]  


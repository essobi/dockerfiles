# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM phusion/baseimage:latest  
MAINTAINER Mateusz Trojak <mateusz.trojak@gmail.com>  
LABEL version="1.1"  
LABEL description="Custom Jenkins Slave Images based on phusion/baseimage with
Java JDK 8, SVN and wget"  
  
# In case you need proxy  
# RUN echo 'Acquire::http::Proxy
"http://proxyuser:proxypwd@proxyip:proxyport";' >> /etc/apt/apt.conf  
# RUN echo 'Acquire::http::Proxy
"https://proxyuser:proxypwd@proxyip:proxyport";' >> /etc/apt/apt.conf  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV TERM xterm  
  
# Add locales after locale-gen as needed  
# Upgrade packages on image  
# Install SSHD, JDK 8 (latest edition) also SVN and wget  
RUN locale-gen en_US.UTF-8 &&\  
apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openjdk-8-jdk &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y subversion --no-
install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y wget --no-install-
recommends &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port for Jenkins connections  
EXPOSE 22  
  
# Default start command  
CMD ["/usr/sbin/sshd", "-D"]  


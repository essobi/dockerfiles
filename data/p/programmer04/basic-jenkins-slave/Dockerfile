# This Dockerfile is used to build a lightweight image containing basic stuff
to be used as a Jenkins slave build node.  
FROM ubuntu:latest  
  
# In case you need proxy  
#RUN echo 'Acquire::http::Proxy "http://127.0.0.1:8080";' >> /etc/apt/apt.conf  
# Set an environment variable only for build  
ARG DEBIAN_FRONTEND="noninteractive"  
# Install required packages  
RUN apt-get -q update &&\  
apt-get -q install -y locales &&\  
apt-get -q install -y --no-install-recommends openssh-server &&\  
rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin  
  
# Setup ssh  
RUN locale-gen en_US.UTF-8 &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Set locale variables in the system  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install JDK (latest edition)  
RUN apt-get -q update &&\  
apt-get -q install -y --no-install-recommends default-jre-headless &&\  
rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin  
  
# Set user:jenkins and password:jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Set bash as a default login shell for user:jenkins  
RUN chsh -s /bin/bash jenkins  
  
# Standard SSH port  
EXPOSE 22  
# Default command  
CMD ["/usr/sbin/sshd", "-D"]  


FROM fedora:23  
MAINTAINER Vojtech Juranek <vjuranek@redhat.com>  
  
# Create Jenkins user and Jenkins group  
RUN groupadd -r radargun -g 1001 && useradd -u 1001 -r -g radargun -m -d
/home/radargun -s /bin/bash -c "RadarGun user" radargun  
RUN echo "radargun:radargun" | chpasswd  
  
# Execute system update  
RUN dnf -y update && dnf clean all  
  
# Install JDK and ssh server  
RUN dnf -y install unzip java-1.8.0-openjdk-devel maven openssh-server which
hostname procps-ng && dnf clean all  
  
# Download and compile RadarGun master  
RUN mkdir /opt/radargun && cd /opt/radargun && curl -o
/opt/radargun/radargun.zip
https://codeload.github.com/radargun/radargun/zip/master && unzip
/opt/radargun/radargun.zip && cd /opt/radargun/radargun-master && mvn clean
install -DskipTests && mv /opt/radargun/radargun-
master/target/distribution/RadarGun-3.0.0-SNAPSHOT/* /opt/radargun/ && rm -rf
/opt/radargun/radargun-master /home/.m2  
  
# Generate ssh key  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
# Add ssh key so we can log in automatically  
ADD radargun-docker.pub /home/radargun/.ssh/authorized_keys  
ADD radargun-docker /home/radargun/.ssh/id_rsa  
ADD radargun-docker.pub /home/radargun/.ssh/id_rsa.pub  
RUN chown -R radargun:radargun /home/radargun/.ssh && chmod 0600
/home/radargun/.ssh/id_rsa /home/radargun/.ssh/authorized_keys  
  
# Additional packages used by 3rh party tools, e.g. Jenkins  
RUN dnf -y install openssh-clients  
  
# Expose standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  


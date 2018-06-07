FROM ubuntu:latest  
MAINTAINER Horace Heaven "hheaven@medullan.com"  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/10gen.list  
  
# Update software package  
RUN apt-get -y update  
  
# Install ssh server  
RUN apt-get -y install openssh-server  
  
# Install java  
RUN apt-get -y install default-jdk  
  
# Install apps  
RUN apt-get -y install nodejs nodejs-legacy npm mongodb-org python-pip xvfb
curl groovy  
  
# Install firefox version 30  
RUN wget
http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/30.0/linux-x86_64/en-
US/firefox-30.0.tar.bz2  
RUN tar -xjvf firefox-30.0.tar.bz2  
RUN mv firefox /opt/firefox30.0  
RUN ln -sf /opt/firefox30.0/firefox /usr/bin/firefox  
  
# Install forever  
RUN npm install -g forever  
  
# Install fleetctl  
RUN wget
https://github.com/coreos/fleet/releases/download/v0.8.1/fleet-v0.8.1-linux-
amd64.tar.gz  
RUN tar -xzf fleet-v0.8.1-linux-amd64.tar.gz; cd fleet-v0.8.1-linux-amd64; mv
fleetctl /usr/bin  
  
# Change the root user's password  
RUN echo "root:password" | chpasswd  
  
# Adds the jenkins user and change the password  
RUN adduser jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Configure ssh  
RUN rm /etc/ssh/ssh_host_rsa_key  
RUN mkdir -p /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
  
# Adding the requirements file with configs to install robot framework and
selenium  
ADD requirements.txt /opt/requirements.txt  
  
# Install robot framework and selenium  
RUN pip install -r /opt/requirements.txt  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd -D"]  


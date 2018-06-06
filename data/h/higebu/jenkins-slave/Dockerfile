FROM ubuntu:trusty  
MAINTAINER Yuya Kusakabe <yuya.kusakabe@gmail.com>  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl git openssh-server openjdk-7-jdk && \  
apt-get clean && \  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd && \  
mkdir -p /var/run/sshd && \  
useradd -ms /bin/bash jenkins && \  
echo "jenkins:jenkins" | chpasswd && \  
curl -s https://get.docker.com/builds/Linux/x86_64/docker-1.8.2 -o
/usr/bin/docker && \  
chmod +x /usr/bin/docker  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  


FROM ubuntu:trusty  
MAINTAINER Ryo Tagami <rtagami@airstrip.jp>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
openjdk-7-jre-headless \  
openssh-server \  
&& \  
DEBIAN_FRONTEND=noninteractive apt-get clean -y && \  
mkdir -p /var/run/sshd && \  
sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional
pam_loginuid.so/g' /etc/pam.d/sshd && \  
useradd -m jenkins && \  
echo "jenkins:jenkins" | chpasswd && \  
printf 'Defaults:jenkins !requiretty\njenkins ALL=(ALL) NOPASSWD:ALL\n' >
/etc/sudoers.d/jenkins && \  
chmod go-rwx /etc/sudoers.d/jenkins  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  


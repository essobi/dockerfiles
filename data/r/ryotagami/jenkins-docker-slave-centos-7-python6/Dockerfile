FROM centos:7  
MAINTAINER Ryo Tagami <rtagami@airstrip.jp>  
  
RUN yum update -y && \  
yum install -y \  
epel-release \  
gcc \  
git \  
initscripts \  
java-1.8.0-openjdk-headless \  
openssh-server \  
python-devel \  
shadow-utils \  
sudo \  
&& \  
yum install -y \  
python-pip \  
python34 \  
python34-devel \  
&& \  
yum clean all && \  
/usr/sbin/sshd-keygen && \  
sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional
pam_loginuid.so/g' /etc/pam.d/sshd && \  
useradd jenkins && \  
echo "jenkins:jenkins" | chpasswd && \  
printf 'Defaults:jenkins !requiretty\njenkins ALL=(ALL) NOPASSWD:ALL\n' >
/etc/sudoers.d/jenkins && \  
chmod go-rwx /etc/sudoers.d/jenkins  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  


FROM node:7.3.0  
MAINTAINER Pedro Maia "felipemoraes@dialhost.com.br"  
RUN DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install openssh-server \  
openjdk-7-jdk \  
git  
  
RUN echo "root:password" | chpasswd && \  
useradd jenkins -m && \  
echo "jenkins:jenkins" | chpasswd  
  
RUN mkdir -p /home/jenkins/.ssh && \  
chown -R jenkins:jenkins /home/jenkins/.ssh  
  
RUN mkdir -p /var/run/sshd && \  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd  
  
RUN npm install -g gulp  
  
CMD ["/usr/sbin/sshd", "-D"]


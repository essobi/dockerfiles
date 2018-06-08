# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM ubuntu:wily  
MAINTAINER kmilner "kmilner@seven10storage.com"  
# Install Oracle Java 8  
RUN \  
# echo "deb http://archive.ubuntu.com/ubuntu wily main universe" >
/etc/apt/sources.list && \  
apt-get update -q && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common
python-software-properties && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update -q && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java8-installer
openssh-server curl lxc vim && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
# clean up tmp install files  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
# Install a basic SSH server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd && \  
# generate a default locale to keep certain warnings at bay  
locale-gen en_US.UTF-8 && \  
# Add user jenkins to the image. Note: the password is encrypted via  
# password="some-good-passwd"; perl -e 'printf("%s\n", crypt($ARGV[0],
"password"))' "$password"  
useradd -s /bin/bash -d /home/jenkins -p "paZMSFlwB0Lw6" jenkins && \  
mkdir -p /home/jenkins && \  
chown -R jenkins:jenkins /home/jenkins && \  
echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
  
COPY bin/setup-docker-and-start-ssh.sh /usr/local/bin/setup-docker-and-start-
ssh.sh  
COPY bin/phone-home.sh /usr/local/bin/phone-home.sh  
  
RUN chmod +x /usr/local/bin/setup-docker-and-start-ssh.sh
/usr/local/bin/phone-home.sh  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/local/bin/setup-docker-and-start-ssh.sh"]  


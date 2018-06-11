FROM ubuntu:latest  
MAINTAINER Stefan Wolf "wolfs@fs.tum.de"  
RUN apt-get install -y software-properties-common && \  
echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get install -y oracle-java7-installer && \  
apt-get install -y openssh-server && \  
apt-get clean && \  
rm -rf /var/cache/oracle-jdk7-installer  
RUN adduser --quiet jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
RUN mkdir /var/run/sshd  
RUN echo 'root:jenkins' | chpasswd  
  
EXPOSE 3333  
CMD /usr/sbin/sshd -D -p 3333  


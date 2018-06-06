# ===================================================  
# Base Dockerfile for all Dandelion images  
# ===================================================  
FROM centos:6.4  
MAINTAINER Thibault Duchateau <thibault.duchateau@gmail.com>  
  
# Install utilities  
RUN yum install -y vim git sudo tar zip bzip2 wget  
  
# Install an SSH server so we can connect to child images  
RUN yum install -y openssh-server && \  
mkdir /var/run/sshd && \  
chkconfig sshd on && \  
service sshd start  
  
# Expose the SSHD port  
EXPOSE 22  
# Configure root and dandelion users  
RUN echo 'root:dandelion' | chpasswd  
RUN groupadd dandelion && \  
useradd -m dandelion -g dandelion && \  
echo 'dandelion:dandelion' | chpasswd && \  
echo 'dandelion ALL=(ALL:ALL) ALL' >> /etc/sudoers  
  
# Install JDK 1.6  
RUN yum install -y java-1.6.0-openjdk  
ENV JAVA_HOME /usr/lib/jvm/java-1.6.0-openjdk.x86_64  
  
# Install Maven  
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-
maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo && \  
yum install -y apache-maven && \  
ln -s /usr/share/apache-maven/bin/mvn /usr/local/bin/mvn  
  
# Install PhantomJS and related utilities  
RUN yum install -y fontconfig freetype && \  
cd /tmp && \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
&& \  
tar xvf phantomjs-1.9.7-linux-x86_64.tar.bz2 && \  
cp /tmp/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin && \  
rm -rf /tmp/phantomjs-1.9.7-linux-x86_64
/tmp/phantomjs-1.9.7-linux-x86_64.tar.bz2  
  
# Install Supervisor and create directory for child images to store
configuration in  
RUN yum install -y python-setuptools && \  
easy_install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
# Add Supervisor base configuration  
ADD supervisord.conf /etc/supervisor/  
  
# Default command  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


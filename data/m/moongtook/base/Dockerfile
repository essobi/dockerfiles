FROM centos:centos6  
MAINTAINER moongtook <moongtook@gmail.com>  
  
# Config root bash  
ADD _bashrc /root/.bashrc  
ADD _bash_profile /root/.bash_profile  
  
# Install EPEL  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install extra utilities  
RUN yum install -y tar python-pip  
  
# Install JDK (Oracle)  
RUN curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.tar.gz
| tar xfz - -C /opt  
ENV JAVA_HOME /opt/jdk1.7.0_71  
RUN alternatives --install /usr/bin/java java /opt/jdk1.7.0_71/bin/java 1  
ADD jdk-7u71.ld.so.conf /etc/ld.so.conf.d/jdk-7u71.ld.so.conf  
RUN ldconfig  


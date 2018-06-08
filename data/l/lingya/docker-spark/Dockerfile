## Apache Spark Base image  
#  
FROM ubuntu:14.04  
MAINTAINER Anton Kirillov anton@bigdata.se  
  
# Setup a volume for data  
VOLUME ["/data"]  
  
# Set correct source list  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-updates main universe"
>> /etc/apt/sources.list  
  
# add the python properties so we can add repos afterwards and also the
utility to auto-accept licenses, some dev tools too  
RUN apt-get update && apt-get upgrade -y && apt-get install -y software-
properties-common debconf-utils rsync openssh-server net-tools vim-tiny sudo
iputils-ping python2.7 less curl  
  
# passwordless ssh  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# auto-acept oracles jdk license  
RUN /bin/echo -e oracle-java7-installer shared/accepted-oracle-license-v1-1
select true | debconf-set-selections  
  
# add JDK7 repository  
RUN add-apt-repository ppa:webupd8team/java  
  
# install Oracle JDK 7  
RUN apt-get update && apt-get upgrade -y && apt-get install -y oracle-
java7-installer  
  
# set java environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# download spark 1.2.0  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.2.0-bin-hadoop2.4.tgz
| tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-1.2.0-bin-hadoop2.4 spark  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $PATH:$SPARK_HOME/bin  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
RUN service ssh start  


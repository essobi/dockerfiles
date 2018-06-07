FROM tianon/centos:6.5  
MAINTAINER Hoseog Lee <hoseog@gmail.com>  
  
ENV HAMA_HOME /opt/hama  
ENV HAMA_VERSION 0.6.4  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum install -y wget \  
which \  
openssh-clients \  
openssh-server \  
curl \  
tar \  
system-config-services \  
sudo  
  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
RUN service sshd start  
  
# java  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie'  
RUN rpm -i jdk-7u71-linux-x64.rpm  
RUN rm jdk-7u71-linux-x64.rpm  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# hama  
RUN wget http://mirror.apache-
kr.org/hama/hama-$HAMA_VERSION/hama-$HAMA_VERSION.tar.gz  
RUN tar -zxvf hama-$HAMA_VERSION.tar.gz  
RUN rm -rf hama-*.tar.gz  
RUN export HAMA_HOME=$HAMA_HOME  
RUN mv hama-* $HAMA_HOME  
  
COPY hama-site.xml $HAMA_HOME/conf/  
  
EXPOSE 40013  


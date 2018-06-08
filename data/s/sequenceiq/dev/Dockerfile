# Create a SequenceIQ development base image  
#  
# docker build -t sequenceiq/dev-docker .  
FROM centos:6.6  
MAINTAINER SequenceIQ  
  
USER root  
  
# add epel  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# install dev tools  
RUN yum install -y curl which tar sudo openssh-server openssh-clients rsync
bunzip2 python tcpdump traceroute net-tools sysstat iperf  
  
# install speedtest-cli  
RUN curl -L https://raw.githubusercontent.com/sivel/speedtest-
cli/master/speedtest_cli.py > /usr/local/bin/speedtest_cli  
RUN chmod +x /usr/local/bin/speedtest_cli  
  
# passwordless ssh  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# java  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie'  
RUN rpm -i jdk-7u51-linux-x64.rpm  
RUN rm jdk-7u51-linux-x64.rpm  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# devel tools  
RUN yum groupinstall "Development Tools" -y  
RUN yum install -y cmake zlib-devel openssl-devel  
  
# maven  
RUN curl http://www.eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz |tar xz -C /usr/share  
ENV M2_HOME /usr/share/apache-maven-3.3.9  
ENV PATH $PATH:$M2_HOME/bin  
  
ENTRYPOINT ["bash"]  


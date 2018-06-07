from stackbrew/ubuntu:saucy  
MAINTAINER Patrick Ting <pcting@gmail.com>  
  
WORKDIR /root/  
  
# Install package with add-apt-repository  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Enable Ubuntu repositories  
RUN add-apt-repository -y multiverse && \  
add-apt-repository -y restricted && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && apt-get upgrade -y  
  
# Install latest Oracle Java from PPA  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer oracle-java7-set-default  
  
# Install SSH server and Zookeeper  
RUN apt-get install -y openssh-server zookeeperd  
  
# Download Hadoop  
RUN wget -q
'http://apache.cs.utah.edu/hadoop/common/hadoop-2.2.0/hadoop-2.2.0.tar.gz'  
  
# Install util packages  
RUN apt-get install -y rsync curl  
  
# Setup system user and group to own and run Hadoop  
RUN addgroup hadoop && adduser --ingroup hadoop hduser  
RUN usermod -a -G hadoop zookeeper  
  
# Setup SSH keys for Hadoop  
RUN su -l -c 'ssh-keygen -t rsa -f /home/hduser/.ssh/id_rsa -P ""' hduser && \  
cat /home/hduser/.ssh/id_rsa.pub | su -l -c 'tee -a
/home/hduser/.ssh/authorized_keys' hduser  
ADD config/ssh-config /home/hduser/.ssh/config  
RUN chmod 600 /home/hduser/.ssh/config  
  
# Fix Ubuntu 13.10 SSH daemon problem with docker:
http://docs.docker.io/en/latest/examples/running_ssh_service/  
RUN sed -ri 's/session[[:blank:]]+required[[:blank:]]+pam_loginuid.so/session
optional pam_loginuid.so/g' /etc/pam.d/sshd  
  
# Deploy and setup file permissions  
RUN tar xvfz /root/hadoop-2.2.0.tar.gz -C /opt && \  
ln -s /opt/hadoop-2.2.0 /opt/hadoop && \  
chown -R root:root /opt/hadoop-2.2.0 && \  
mkdir /opt/hadoop-2.2.0/logs && \  
chown -R hduser:hadoop /opt/hadoop-2.2.0/logs  
  
# Setup hduser environment  
ADD config/bashrc /home/hduser/.bashrc  
  
# Configure Hadoop  
ADD config/core-site.xml /tmp/hadoop-etc/core-site.xml  
ADD config/yarn-site.xml /tmp/hadoop-etc/yarn-site.xml  
ADD config/mapred-site.xml /tmp/hadoop-etc/mapred-site.xml  
ADD config/hdfs-site.xml /tmp/hadoop-etc/hdfs-site.xml  
  
RUN mv /tmp/hadoop-etc/* /opt/hadoop/etc/hadoop/  
  
# Expose SSHD  
EXPOSE 22  
# QuorumPeerMain (Zookeeper)  
EXPOSE 2181 39534  
# NameNode (HDFS)  
EXPOSE 9000 50070  
# DataNode (HDFS)  
EXPOSE 50010 50020 50075  
# SecondaryNameNode (HDFS)  
EXPOSE 50090  
# ResourceManager (YARN)  
EXPOSE 8030 8031 8032 8033 8088  
# NodeManager (YARN)  
EXPOSE 8040 8042 13562 47784  
# JobHistoryServer  
EXPOSE 10020 19888  
# Create start script  
ADD config/run-hadoop.sh /root/run-hadoop.sh  
RUN chmod +x /root/run-hadoop.sh  
  
CMD ["/root/run-hadoop.sh"]  


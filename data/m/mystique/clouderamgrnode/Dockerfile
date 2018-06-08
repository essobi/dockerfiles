##################################################################################  
##  
## VERSION :0.0.1  
## DATE :28Aug2015  
##  
## DESCRIPTION :"This image installs ssh, updates centos6.6 and install
Cloudera Manager  
##  
## Ref [1] : https://github.com/dgreco/cdh_docker/blob/master/Dockerfile  
## Ref [2] : https://registry.hub.docker.com/u/sequenceiq/hadoop-
docker/dockerfile/  
##  
##################################################################################  
FROM centos:6.6  
MAINTAINER mystique <miztiik@gmail.com>  
  
# Setup yum to use caching in the shared folder to allow it to be reused by
multiple systems, number of copies to 3 & Enable the fastest mirror  
RUN sed -ri 's/keepcache=0/keepcache=1/g' /etc/yum.conf && \  
sed -ri 's/installonly_limit=5/installonly_limit=3/g' /etc/yum.conf && \  
sed -ri 's/enabled=1/enabled=0/g' /etc/yum/pluginconf.d/fastestmirror.conf  
  
# Have to really escape the special chracters will back slashes, probably
should find a neater way of doing this, (laterz..)  
RUN sed -ri
's/cachedir=\/var\/cache\/yum\/\$basearch\/\$releasever/cachedir=\/media\/sf_dockerRepos\/dockerTmp\/yum\/\$basearch\/\$releasever/g'
/etc/yum.conf  
  
# Lets install the necessary binaries  
RUN yum -y update && \  
yum -y install epel-release \  
yum-presto \  
openssh openssh-server \  
openssh-clients \  
which \  
tar \  
wget \  
rsync \  
sudo && \  
yum clean all  
  
# Set up SSHD config  
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g'
/etc/ssh/sshd_config && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# Setting up password less authentication  
RUN sed -ri "s/# PasswordAuthentication yes/PasswordAuthentication no/"
/etc/ssh/sshd_config  
  
# Change the value to no; this will prevent the question when connecting with
SSH to the host.  
RUN sed -ri "s/# StrictHostKeyChecking ask/StrictHostKeyChecking no/"
/etc/ssh/ssh_config  
  
# Disable ip tables & Set sshd to start by default, Generates keys on the
first run  
RUN chkconfig iptables off && \  
chkconfig sshd on && \  
mkdir /var/run/sshd && \  
/etc/init.d/sshd start  
  
## Cloudera Manager Installation Begins ##  
# Create an user and set it to sudo to root without password  
RUN useradd hadoopadmin -G wheel -d /home/hadoopadmin -s /bin/bash && \  
echo 'hadoopadmin:tcuser' | chpasswd && \  
echo '%wheel ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
# Set up SSH passwordless ssh ( First time start up of sshd will create these
keys)  
RUN mkdir /home/hadoopadmin/.ssh && \  
ssh-keygen -q -N "" -t rsa -f /home/hadoopadmin/.ssh/id_rsa && \  
cp /home/hadoopadmin/.ssh/id_rsa.pub /home/hadoopadmin/.ssh/authorized_keys &&
\  
chmod 600 /home/hadoopadmin/.ssh/authorized_keys; chmod 700
/home/hadoopadmin/.ssh && \  
chown -R hadoopadmin:hadoopadmin /home/hadoopadmin/.ssh  
  
# Install Cloudera Manager Repo & Cloudera Hadoop 5 packages  
RUN cd /etc/yum.repos.d/ && \  
curl -O http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-
manager.repo && \  
curl -O http://archive.cloudera.com/cdh5/one-click-
install/redhat/6/x86_64/cloudera-cdh-5-0.x86_64.rpm && \  
yum -y --nogpgcheck localinstall cloudera-cdh-5-0.x86_64.rpm && \  
rpm --import http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/RPM-GPG-KEY-
cloudera  
  
# Install Java (might need to be changed to the latest uri)  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie' && \  
yum -y install jdk-8u45-linux-x64.rpm && \  
rm -rf jdk-8u45-linux-x64.rpm  
  
# Installing the Cloudera Manager Daemons & Start the DB service to allow it
configure the DB & services  
RUN yum -y install cloudera-manager-server-db-2 \  
cloudera-manager-daemons \  
cloudera-manager-server && \  
yum clean all  
  
# I dont think we need to install agent on manager server  
# RUN yum -y install cloudera-manager-agent && yum clean all  
# Expose the private port for mapping ( Need to trim them accordingly after
checking them out)  
EXPOSE 22 2181 7180 7182 50010 50075 50020 8020 50070 50090 8032 8030 8031
8033 8088 8888 8040 8042 8041 10020 19888 41370 38319 10000 21050 25000 25010
25020 18080 18081 7077 7078 9000 9001  
# Start the SSH daemon  
CMD [ "/usr/sbin/sshd", "-D" ]  


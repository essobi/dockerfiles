# Setup base image for the ThinkIQ hadoop images  
# the image also includes zookeeper  
FROM ubuntu:14.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
ENV ZK_VERSION=3.4.9 JAVA_HOME=/usr/lib/jvm/default-java  
COPY sleep.sh /usr/local/bin/sleep.sh  
# install base system, with preconfigured hadoop user  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-get update && \  
apt-get install -y sudo curl tar sudo openssh-server openssh-client rsync ntp
&& \  
groupadd -r hadoop && sudo useradd hduser -s /bin/bash -g sudo -m && \  
rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key /root/.ssh/id_rsa &&
\  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \  
ps -ef | grep sshd && \  
/etc/init.d/ntp stop && \  
ps -ef | grep ntp && \  
/usr/sbin/ntpdate pool.ntp.org && \  
/etc/init.d/ntp start && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-
selections && \  
apt-get install -y oracle-java8-installer && \  
cd /usr/lib/jvm/ && \  
ln -s java-8-oracle default-java && \  
apt-get build-dep pkg-config -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
echo "root ALL=(ALL) ALL" > /etc/sudoers && \  
echo "hduser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
echo "Defaults env_reset" >>/etc/sudoers && \  
echo "Defaults
secure_path=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
>> /etc/sudoers && \  
echo "export JAVA_HOME=/usr/lib/jvm/default-java" > /etc/profile.d/java.sh &&
\  
chmod 440 /etc/sudoers && \  
cd /tmp && \  
wget
http://apache.mirrors.pair.com/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
&& \  
tar -zxvf zookeeper-${ZK_VERSION}.tar.gz && \  
rm zookeeper-${ZK_VERSION}.tar.gz && \  
mv /tmp/zookeeper-${ZK_VERSION} /usr/local/ && \  
ln -s /usr/local/zookeeper-${ZK_VERSION} /usr/local/zookeeper && \  
groupadd -r zookeeper && useradd -r -g zookeeper zookeeper && \  
mkdir -p /var/lib/zookeeper && \  
chown -R hduser:hadoop /var/lib/zookeeper /usr/local/zookeeper-${ZK_VERSION}
&& \  
chmod -R 0755 /usr/local/zookeeper/ && \  
chmod 777 /var/lib && \  
chmod 0755 /usr/local/bin/sleep.sh && \  
echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf && \  
echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf && \  
echo "net.ipv6.conf.lo.disable_ipv6 = 1" >> /etc/sysctl.conf  
  
EXPOSE 2181 2888 3888  
  
VOLUME ["/var/lib/zookeeper"]  
  
USER hduser  
WORKDIR /home/hduser  
  
RUN ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa && \  
cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys && \  
echo " StrictHostKeyChecking no" >> ~/.ssh/config && \  
sudo chmod 400 ~/.ssh/config && \  
chmod 0600 ~/.ssh/authorized_keys && \  
ps -ef | grep sshd  
  
RUN echo "tickTime=2000" > /usr/local/zookeeper-${ZK_VERSION}/conf/zoo.cfg &&
\  
echo "initLimit=5" >> /usr/local/zookeeper-${ZK_VERSION}/conf/zoo.cfg && \  
echo "syncLimit=2" >> /usr/local/zookeeper-${ZK_VERSION}/conf/zoo.cfg && \  
echo "clientPort=2181" >> /usr/local/zookeeper-${ZK_VERSION}/conf/zoo.cfg && \  
echo "dataDir=/var/lib/zookeeper" >>
/usr/local/zookeeper-${ZK_VERSION}/conf/zoo.cfg  
  
EXPOSE 22


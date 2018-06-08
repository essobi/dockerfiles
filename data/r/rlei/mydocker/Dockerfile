FROM centos:7.2.1511  
MAINTAINER Radar Lei <rlei@pivotal.io>  
  
# install document with yum  
RUN sed -i 's/tsflags=nodocs//g' /etc/yum.conf  
  
# add epel repo  
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-9.noarch.rpm  
  
# install all software we need  
RUN yum makecache && \  
yum install -y man passwd sudo tar which git mlocate links make bzip2 net-
tools \  
autoconf automake libtool m4 gcc gcc-c++ gdb bison flex gperf maven indent \  
libuuid-devel krb5-devel libgsasl-devel expat-devel libxml2-devel \  
perl-ExtUtils-Embed pam-devel python-devel libcurl-devel snappy-devel \  
thrift-devel libyaml-devel libevent-devel bzip2-devel openssl-devel \  
openldap-devel protobuf-devel readline-devel net-snmp-devel apr-devel \  
libesmtp-devel python-pip json-c-devel \  
java-1.7.0-openjdk-devel lcov cmake R-core-devel \  
openssh-clients openssh-server perl-JSON && \  
yum clean all  
  
RUN pip --retries=50 --timeout=300 install pycrypto  
  
# Unalias default alias for 'cp, mv, rm'.  
RUN sed -i '/^alias/d' /root/.bashrc  
  
# Install higher version cmake, 3.0+  
RUN mkdir /tmp/cmake; pushd /tmp/cmake ; \  
curl -O https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz; \  
tar xzvf cmake-3.7.2-Linux-x86_64.tar.gz; \  
cp -rf cmake-3.7.2-Linux-x86_64/* /usr/ ; \  
cmake --version; popd;  
  
# setup ssh server and keys for root  
RUN sshd-keygen && \  
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
chmod 0600 ~/.ssh/authorized_keys  
  
# setup JAVA_HOME for all users  
RUN echo "#!/bin/sh" > /etc/profile.d/java.sh && \  
echo "export JAVA_HOME=/etc/alternatives/java_sdk" >> /etc/profile.d/java.sh
&& \  
chmod a+x /etc/profile.d/java.sh  
  
# create user gpadmin since HAWQ cannot run under root  
RUN groupadd -g 1000 gpadmin && \  
useradd -u 1000 -g 1000 gpadmin && \  
echo "gpadmin ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/gpadmin  
  
# sudo should not require tty  
RUN sed -i -e 's|Defaults requiretty|#Defaults requiretty|' /etc/sudoers  
  
ENV BASEDIR /data  
RUN mkdir -p /data && chmod 777 /data  
  
USER gpadmin  
  
# setup ssh client keys for gpadmin  
RUN ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
chmod 0600 ~/.ssh/authorized_keys  
  
USER root  
  
WORKDIR /data  


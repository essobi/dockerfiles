# sshd  
#  
# VERSION 0.0.1  
FROM ubuntu:trusty  
#MAINTAINER Thatcher R. Peskens "thatcher@dotcloud.com"  
# install ssh only for debugging  
RUN \  
apt-get update && \  
apt-get -y install openssh-server && \  
mkdir /var/run/sshd && \  
echo 'root:QAP@SSw0rd' | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
EXPOSE 22  
#RUN apt-get -y install python-software-properties  
#RUN apt-get -y install software-properties-common  
RUN apt-get install -y build-essential  
RUN apt-get install -y openssl libreadline6 libreadline6-dev curl zlib1g
zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-
dev autoconf libc6-dev ncurses-dev automake libtool bison subversion pkg-
config  
  
# install ruby dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
zlib1g-dev \  
libssl-dev \  
libreadline6-dev \  
libyaml-dev  
  
# install ruby from source and cleanup afterward (from murielsalvan/ruby)  
ADD http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.4.tar.gz /tmp/  
RUN cd /tmp && \  
tar -xzf ruby-2.1.4.tar.gz && \  
cd ruby-2.1.4 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -rf ruby-2.1.4 && \  
rm -f ruby-2.1.4.tar.gz  
  
# install docker  
#RUN apt-get update && \  
# apt-get -y install docker.io && \  
# ln -sf /usr/bin/docker.io /usr/local/bin/docker && \  
# sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io && \  
# update-rc.d docker.io defaults  
RUN apt-get -y install vim  
RUN gem install pry-byebug  
RUN gem install net-ssh  


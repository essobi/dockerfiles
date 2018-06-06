FROM ubuntu:14.04  
MAINTAINER Coverit <support@coverit.io>  
  
# RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted
universe multiverse" > /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list  
# Install mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list && \  
apt-get update && \  
apt-get install -y mongodb-org  
  
# Install wget  
RUN apt-get install -y wget  
  
# Install curl  
RUN apt-get install -y curl  
  
# Install git  
RUN apt-get install -y git  
  
# Install golang  
RUN wget -q https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz
&& \  
tar -C /usr/local -xzf go1.4.2.linux-amd64.tar.gz && \  
rm go1.4.2.linux-amd64.tar.gz  
ENV GOPATH /go  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  
  
# Install godep  
RUN go get github.com/tools/godep  
  
# Install node.js  
RUN apt-get install -y build-essential && \  
wget -qO- https://github.com/taaem/nodejs-linux-
installer/releases/download/0.2/node-install.sh | bash  
  
# Install lcov and gcc4.4, for test env of coverit-cli  
RUN apt-get install -y lcov gcc-4.4 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50 --slave
/usr/bin/gcov gcov /usr/bin/gcov-4.8 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.4 60 --slave
/usr/bin/gcov gcov /usr/bin/gcov-4.4  


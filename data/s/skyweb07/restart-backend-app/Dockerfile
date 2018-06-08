############################################################  
# Dockerfile to build restart application  
# Based on Vapor docker image  
############################################################  
  
FROM ubuntu:14.04  
  
# Set environment variables for image  
ENV SWIFT_SNAPSHOT swift-3.1.1-RELEASE  
ENV SWIFT_SNAPSHOT_LOWERCASE swift-3.1.1-release  
ENV UBUNTU_VERSION ubuntu14.04  
ENV UBUNTU_VERSION_NO_DOTS ubuntu1404  
ENV HOME /root  
ENV WORK_DIR /root  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Linux OS utils and libraries  
RUN apt-get update && apt-get install -y \  
clang \  
binutils \  
git \  
libicu-dev \  
wget \  
libxml2 \  
libcurl3 \  
curl && \  
rm -r /var/lib/apt/lists/*  
  
# Install Swift compiler  
RUN wget
https://swift.org/builds/$SWIFT_SNAPSHOT_LOWERCASE/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz
\  
&& tar xzvf $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz \  
&& rm $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz  
ENV PATH $WORK_DIR/$SWIFT_SNAPSHOT-$UBUNTU_VERSION/usr/bin:$PATH  
RUN swiftc -h  
  
# Install MySQL  
# RUN apt-get update && apt-get install -y \  
# libmysqlclient-dev  
  
RUN export DEBIAN_FRONTEND=noninteractive  
  
RUN wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb  
RUN dpkg -i mysql-apt-config_0.6.0-1_all.deb  
RUN apt-get update  
RUN apt-get install mysql-server -y  
  
# # Install SQLite  
# RUN apt-get update && \  
# apt-get install -y libsqlite3-dev && \  
# rm -r /var/lib/apt/lists/* \  
  
# Install Vapor Toolbox  
RUN apt-get update && \  
apt-get install -y wget software-properties-common python-software-properties
apt-transport-https && \  
wget https://repo.vapor.codes/apt/keyring.gpg -O- | apt-key add - && \  
echo "deb https://repo.vapor.codes/apt trusty main" | tee
/etc/apt/sources.list.d/vapor.list && \  
apt-get update && \  
apt-get install -y vapor && \  
apt-get install -y ctls cmysql && \  
rm -r /var/lib/apt/lists/*  
  
# Set work dir to /  
WORKDIR /  
  
EXPOSE 8080


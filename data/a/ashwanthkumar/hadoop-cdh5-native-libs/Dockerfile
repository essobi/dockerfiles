FROM ubuntu:14.04.3  
MAINTAINER Ashwanth Kumar <ashwanthkumar@googlemail.com>  
  
ENV CDH5_VERSION=hadoop-2.6.0-cdh5.14.0  
ENV APP_DIR=/app  
WORKDIR $APP_DIR  
  
## Install Base dependencies  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y wget pkg-config gcc g++ cmake make automake autoconf
zlib1g-dev libssl-dev openjdk-7-jdk maven  
  
## Install the specific version of protobuf  
RUN wget
https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz
&& \  
tar xzf protobuf-2.5.0.tar.gz && \  
rm -rf protobuf-2.5.0.tar.gz && \  
cd protobuf-2.5.0 && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
## Download and compile hadoop native libraries from source  
RUN wget --continue
http://archive.cloudera.com/cdh5/cdh/5/${CDH5_VERSION}-src.tar.gz && \  
tar xzf ${CDH5_VERSION}-src.tar.gz && \  
cd ${CDH5_VERSION} && \  
mvn package -Pdist,native -DskipTests -Dtar && \  
cd hadoop-dist/target && \  
tar -czf hadoop-native-${CDH5_VERSION}.tar.gz ${CDH5_VERSION}/lib && \  
cp hadoop-native-${CDH5_VERSION}.tar.gz ${APP_DIR}/ && \  
rm -rf ${APP_DIR}/${CDH5_VERSION} ${APP_DIR}/${CDH5_VERSION}-src.tar.gz  


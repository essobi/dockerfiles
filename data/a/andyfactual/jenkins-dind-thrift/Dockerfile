FROM cmbleakley/docker-jenkins-dind:latest  
  
RUN apt-get update && \  
apt-get install -y \  
ant \  
automake \  
bison \  
flex \  
g++ \  
git \  
libboost1.55-all-dev \  
libevent-dev \  
libssl-dev \  
libtool \  
make \  
pkg-config && \  
mkdir /root/thrift && \  
curl -f http://archive.apache.org/dist/thrift/0.9.2/thrift-0.9.2.tar.gz >
/root/thrift/thrift-0.9.2.tar.gz && \  
tar -xzf /root/thrift/thrift-0.9.2.tar.gz -C /root/thrift && \  
cd /root/thrift/thrift-0.9.2 && \  
./configure --with-java --without-cpp --without-python --without-ruby && \  
make && \  
make install && \  
cd -  
  
RUN add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk && \  
# old version of update-java-alternatives doesn't work with new jinfo format  
# see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=825987  
sed -i "s/jdkhl/jdk/g" /usr/lib/jvm/.java-1.8.0-openjdk-amd64.jinfo && \  
update-java-alternatives -s java-1.8.0-openjdk-amd64  


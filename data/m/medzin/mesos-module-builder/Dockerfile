FROM ubuntu:trusty  
MAINTAINER Adam Medziński <adam.medzinski@gmail.com>  
  
# install dependencies  
RUN apt-get update  
RUN apt-get -y install \  
build-essential \  
autoconf \  
automake \  
cmake \  
wget \  
git-core \  
libsasl2-dev \  
libsasl2-modules-gssapi-heimdal \  
libtool \  
libsvn-dev \  
libapr1-dev \  
make \  
python \  
libpython-dev \  
python-dev \  
unzip \  
libssl-dev \  
ca-certificates \  
libcurl4-openssl-dev \  
\--no-install-recommends  
  
# install mesos  
RUN mkdir -p /tmp  
  
WORKDIR /tmp  
RUN wget https://archive.apache.org/dist/mesos/1.3.0/mesos-1.3.0.tar.gz && \  
tar -xvzf mesos-1.3.0.tar.gz && \  
mv mesos-1.3.0 /mesos && \  
rm mesos-1.3.0.tar.gz  
WORKDIR /mesos  
RUN mkdir build  
WORKDIR build  
RUN ../configure \  
\--disable-java \  
\--disable-optimize \  
\--without-included-zookeeper  
RUN make install  
RUN ldconfig  
  
# prepare place for mesos module build  
WORKDIR /module  
VOLUME /module  
ENTRYPOINT mkdir -p build && cd build && cmake .. && make && make test  


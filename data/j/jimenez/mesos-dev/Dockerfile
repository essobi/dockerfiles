#Mesos image from clang 3.4  
FROM jimenez/clang  
MAINTAINER Isabel Jimenez <contact@isabeljimenez.com>  
  
RUN apt-get update -q  
  
#Install Dependencies  
RUN apt-get -qy install \  
autoconf \  
automake \  
ca-certificates \  
clang-format-3.5 \  
git-core \  
libapr1-dev \  
libcurl4-nss-dev \  
libsasl2-dev \  
libsasl2-modules \  
libsvn-dev \  
libtool \  
zlib1g-dev \  
\--no-install-recommends  
  
#Creating a Mesos repository  
RUN mkdir /mesos && chown daemon /mesos  
  
WORKDIR /mesos  
  
#Clone mesos repository  
RUN git clone http://git-wip-us.apache.org/repos/asf/mesos.git .  
  
#Bootstrap  
RUN ./bootstrap  
  
#Configure  
RUN mkdir build && cd build && ../configure --disable-java --disable-python
--disable-optimize --without-included-zookeeper  
  
#Make  
RUN cd build && make -j 4  


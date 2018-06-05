FROM ubuntu:trusty  
MAINTAINER gecko3262@gmail.com  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:george-edison55/cmake-3.x \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
cmake \  
git-core \  
zlib1g-dev \  
libbz2-dev \  
openssl \  
libssl-dev \  
libmysqlclient-dev \  
libmysql++-dev \  
libreadline6-dev \  
libboost1.55-dev \  
libboost-iostreams1.55-dev \  
libboost-thread1.55-dev \  
libboost-system1.55-dev \  
libboost-filesystem1.55-dev \  
libboost-program-options1.55-dev \  
clang-3.5 \  
&& rm -rf /build/* \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /usr/share/doc/* \  
&& rm -rf /var/lib/apt/lists/*  
  


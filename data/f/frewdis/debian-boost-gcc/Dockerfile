FROM debian:stretch  
MAINTAINER gecko3262@gmail.com  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
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
libboost1.58-dev \  
libboost-iostreams1.58-dev \  
libboost-thread1.58-dev \  
libboost-system1.58-dev \  
libboost-filesystem1.58-dev \  
libboost-program-options1.58-dev \  
&& rm -rf /build/* \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /usr/share/doc/* \  
&& rm -rf /var/lib/apt/lists/*  


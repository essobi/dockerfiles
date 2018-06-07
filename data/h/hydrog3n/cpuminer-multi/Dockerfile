FROM debian:stretch-slim  
  
MAINTAINER Hydrog3n <contact@loicvaille.ovh>  
  
# update apt cache  
RUN apt-get update  
  
# install packages  
RUN apt-get install -y git \  
build-essential \  
automake \  
autoconf \  
pkg-config \  
libcurl4-openssl-dev \  
libjansson-dev \  
libssl-dev \  
zlib1g-dev \  
libgmp-dev \  
make \  
g++ \  
&& cd /tmp \  
&& git clone https://github.com/tpruvot/cpuminer-multi.git \  
&& cd cpuminer-multi \  
&& chmod +x build.sh \  
&& ./build.sh \  
&& cp cpuminer /usr/local/bin/ \  
&& chmod +x /usr/local/bin/cpuminer \  
&& apt-get purge -y git automake make pkg-config autoconf g++ \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/cache/debconf/*-old  
  
# run minerd  
COPY entrypoint.sh /  
  
RUN mkdir /config  
  
VOLUME /config  
  
RUN ["chmod", "+x", "/entrypoint.sh"]  
ENTRYPOINT ["./entrypoint.sh"]


FROM debian:stretch-slim  
  
MAINTAINER Hydrog3n <contact@loicvaille.ovh>  
  
# update apt cache  
RUN apt-get update  
  
# install packages  
RUN apt-get install -y git build-essential autoconf libcurl4-openssl-dev \  
&& cd /tmp \  
&& git clone https://github.com/elmad/darkcoin-cpuminer-1.3-avx-aes.git \  
&& cd darkcoin-cpuminer-1.3-avx-aes \  
&& chmod +x autogen.sh \  
&& ./autogen.sh \  
&& ./configure CFLAGS="-O3 -march=native" \  
&& make && make install \  
&& apt-get purge -y git cmake autoconf \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/cache/debconf/*-old  
  
# run minerd  
COPY entrypoint.sh /  
  
RUN mkdir /config  
  
VOLUME /config  
  
RUN ["chmod", "+x", "/entrypoint.sh"]  
ENTRYPOINT ["./entrypoint.sh"]


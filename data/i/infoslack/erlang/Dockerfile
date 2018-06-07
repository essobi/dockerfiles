FROM debian:jessie  
  
MAINTAINER Daniel Romero <infoslack@gmail.com>  
  
ENV OTP_VERSION=18.1  
ENV LANG=C.UTF-8  
  
RUN buildDeps=" \  
autoconf \  
bison \  
ca-certificates \  
curl \  
gcc \  
g++ \  
libbz2-dev \  
libgdbm-dev \  
libglib2.0-dev \  
libncurses-dev \  
libodbc1 \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
unixodbc-dev \  
make \  
"; \  
apt-get update && apt-get install -y --no-install-recommends $buildDeps \  
&& curl -SL "http://www.erlang.org/download/otp_src_$OTP_VERSION.tar.gz" -o
erlang.tar.gz \  
&& mkdir -p /usr/src/erlang \  
&& tar -xvf erlang.tar.gz -C /usr/src/erlang --strip-components=1 \  
&& rm erlang.tar.gz \  
&& cd /usr/src/erlang \  
&& ./otp_build autoconf \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
&& find /usr/local -name examples |xargs rm -rf \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /usr/src/otp-src /var/lib/apt/lists/*  
  
CMD ["erl"]  


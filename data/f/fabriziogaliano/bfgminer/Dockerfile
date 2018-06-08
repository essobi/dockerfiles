FROM ubuntu:16.04  
# ENV BFG_USER ""  
# ENV BFG_PASSWORD ""  
# ENV BFG_URL ""  
USER root  
  
COPY ./docker /docker  
  
RUN apt update -dd  
RUN apt install -y \  
supervisor \  
build-essential \  
autoconf \  
automake \  
libtool \  
pkg-config \  
libcurl4-gnutls-dev \  
libjansson-dev \  
uthash-dev \  
libncursesw5-dev \  
libudev-dev \  
libusb-1.0-0-dev \  
libevent-dev \  
libmicrohttpd-dev \  
git  
  
RUN cd /home \  
&& git clone https://github.com/luke-jr/bfgminer.git  
  
RUN cd /home/bfgminer \  
&& ./autogen.sh \  
&& ./configure \  
\--enable-scrypt \  
\--enable-sha256d \  
\--enable-gridseed \  
\--enable-bfsb \  
\--enable-jingtian \  
\--enable-metabank \  
\--enable-minergate \  
\--enable-minion \  
\--enable-titan \  
\--enable-zeusminer \  
&& make  
  
#ENTRYPOINT ["/bin/bash", "/docker/scripts/entrypoint.sh"]  
#CMD ["/bin/bash", "/docker/scripts/start-mining.sh"]  


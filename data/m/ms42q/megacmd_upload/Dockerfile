FROM debian  
WORKDIR /root/  
RUN apt-get update && \  
apt-get install \  
git \  
autoconf \  
libtool \  
g++ \  
libcrypto++-dev \  
libz-dev \  
libsqlite3-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
libreadline-dev libpcre++-dev libsodium-dev \  
libc-ares-dev \  
make \  
gpg \  
libfreeimage-dev -y && \  
apt-get clean  
  
RUN git clone https://github.com/meganz/sdk.git && \  
cd sdk && \  
git checkout 4edf31a82e12e03639c8eee31851fa82e37d6675 && \  
sh autogen.sh && \  
./configure --prefix=/usr/ && \  
make && \  
make install && \  
cd .. && \  
rm -rf sdk  
  
COPY entrypoint.sh entrypoint.sh  
  
ENV TARGET /upload  
ENV USERNAME NOBODY  
ENV PASSWORD CHANGEME  
ENV GPG_ID NONE  
ENV PREFIX upload-from-docker  
  
ENTRYPOINT bash ./entrypoint.sh  


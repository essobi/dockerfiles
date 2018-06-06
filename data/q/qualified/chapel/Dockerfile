FROM debian:stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
wget \  
ca-certificates \  
gcc \  
g++ \  
perl \  
python \  
libgmp10 \  
libgmp-dev \  
bash \  
make \  
mawk \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
ENV CHPL_HOST_PLATFORM=linux64 \  
CHPL_GMP=system  
  
RUN set -ex; \  
cd /tmp; \  
wget -q https://github.com/chapel-
lang/chapel/releases/download/1.16.0/chapel-1.16.0-1.tar.gz; \  
echo "8a12c0a90d7fbef5d2bc969a578e58f6d2619f501a76fe470f80762e2fb0386e
*chapel-1.16.0-1.tar.gz" | sha256sum -c -; \  
mkdir chapel; \  
tar zxf chapel-1.16.0-1.tar.gz -C chapel --strip-components=1; \  
rm chapel-1.16.0-1.tar.gz; \  
cd chapel; \  
./configure --prefix=/usr; \  
make -j 4; \  
make install; \  
rm -rf /tmp/chapel;  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
WORKDIR /workspace  


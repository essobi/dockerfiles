FROM debian:jessie  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
make g++ wget libaio-dev libapparmor-dev libattr1-dev \  
libbsd-dev libcap-dev libgcrypt11-dev libkeyutils-dev \  
libsctp-dev zlib1g-dev && \  
wget --no-check-certificate https://github.com/ColinIanKing/stress-
ng/archive/V0.08.02.tar.gz && \  
tar xfz V0.08.02.tar.gz && \  
mv stress-ng* /stress-ng && \  
make -C /stress-ng && \  
mv /stress-ng/stress-ng /usr/bin && \  
rm -r /stress-ng && \  
apt-get purge -y make g++ wget && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD entrypoint.sh /root  
  
ENTRYPOINT ["/root/entrypoint.sh"]  


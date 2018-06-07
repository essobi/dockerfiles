FROM debian:latest  
MAINTAINER SYA-KE <syakesaba@gmail.com>  
  
ENV HOSTAPD_URL https://w1.fi/releases/hostapd-2.6.tar.gz  
ENV HOSTAPD_WPE_URL https://github.com/syakesaba/hostapd-wpe.git  
  
RUN apt-get update && \  
apt-get install -y openssl libssl-dev libnl-3-dev libnl-genl-3-dev build-
essential git wget libnfnetlink-dev libsqlite3-dev vim && \  
apt-get clean  
  
RUN git clone $HOSTAPD_WPE_URL && \  
cd hostapd-wpe && \  
wget $HOSTAPD_URL && \  
tar xzvf hostapd-2.6.tar.gz && \  
patch -p0 < hostapd-wpe-2.6-user.patch && \  
cd hostapd-2.6/hostapd && \  
make install  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


FROM kalilinux/kali-linux-docker  
  
# Install dependancies  
RUN apt-get update && apt-get install -y make pkgconf libnl-genl-3-dev build-
essential git wget libssl1.0-dev  
  
RUN cd /root && \  
git clone https://github.com/OpenSecurityResearch/hostapd-wpe && \  
wget http://hostap.epitest.fi/releases/hostapd-2.6.tar.gz && \  
tar -zxf hostapd-2.6.tar.gz && \  
cd hostapd-2.6 && \  
patch -p1 < ../hostapd-wpe/hostapd-wpe.patch && \  
cd hostapd && \  
make && \  
cd ../../hostapd-wpe/certs && \  
./bootstrap && \  
cd ../../hostapd-2.6/hostapd  
  
ENV PATH="/root/hostapd-2.6/hostapd/:$PATH"  
WORKDIR /root/hostapd-2.6/hostapd  
  
CMD ["hostapd-wpe","/conf/hostapd-wpe.conf"]  


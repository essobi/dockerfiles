FROM gliderlabs/alpine  
  
MAINTAINER chinch --> n65ghz@gmail.com <\--  
  
ADD wuds.tar.gz /  
  
WORKDIR wuds/  
  
RUN apk update && \  
apk upgrade && \  
apk add git python iw python-dev libpcap-dev gcc g++ wget && \  
wget https://bootstrap.pypa.io/ez_setup.py -O - | python && \  
git clone https://github.com/CoreSecurity/pcapy.git && \  
cd pcapy && \  
python setup.py install && \  
rm -rf win32 && \  
cd .. && \  
rm -rf setuptools-24.0.2.zip && \  
apk del --purge gcc git wget g++ tar && \  
rm -rf /var/cache/apk && \  
cp /wuds/libstdc++.so.6 /usr/lib && \  
cp /wuds/libstdc++.so.6.0.21 /usr/lib && \  
cp /wuds/libgcc_s.so.1 /usr/lib && \  
cp /wuds/libpcap.so.1 /usr/lib && \  
cp /wuds/libpython2.7.so.1.0 /usr/lib && \  
rm -rf libstdc++.so.6 libstdc++.so.6.0.21 libgcc_s.so.1 libpcap.so.1
libpython2.7.so.1.0  
  
ENV PATH=$PATH:/wuds/pcapy  
  
ENTRYPOINT /wuds/run  
  
  


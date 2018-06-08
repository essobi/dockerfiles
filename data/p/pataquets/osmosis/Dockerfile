FROM java  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install wget \  
&& \  
wget --output-document=/tmp/osmosis-latest.tgz
http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz && \  
cd /tmp/ && \  
tar xvf osmosis-latest.tgz && \  
rm -v /tmp/osmosis-latest.tgz \  
&& \  
mv -v /tmp/bin/* /usr/bin/ && \  
mv -v /tmp/config /etc/osmosis && \  
mv -v /tmp/lib/default /usr/share/osmosis && \  
mv -v /tmp/script /usr/share/osmosis && \  
mkdir -vp /usr/share/doc/osmosis && \  
mv -v /tmp/*.txt /usr/share/doc/osmosis && \  
rmdir /tmp/bin/ /tmp/lib/ && \  
cd - \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
ENTRYPOINT [ "osmosis" ]  


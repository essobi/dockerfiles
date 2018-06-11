FROM tozd/runit  
  
VOLUME /var/log/tunneldigger  
  
ENV TUNNELDIGGER_UUID=  
ENV TUNNELDIGGER_BROKERS=  
ENV TUNNELDIGGER_LIMIT_BW_DOWN=  
ENV TUNNELDIGGER_BRIDGE=  
  
RUN apt-get update -q -q && \  
apt-get install git build-essential libnl-dev iproute2 --yes --force-yes && \  
git clone https://github.com/wlanslovenija/tunneldigger.git /tmp/tunneldigger-
build && \  
cd /tmp/tunneldigger-build/client && \  
make && \  
cp l2tp_client /usr/local/bin/tunneldigger && \  
rm -rf /tmp/tunneldigger-build && \  
apt-get purge git build-essential --yes --force-yes && \  
apt-get autoremove --yes --force-yes  
  
COPY ./etc /etc  


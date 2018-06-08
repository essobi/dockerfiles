FROM bitnami/minideb  
  
ENV MULTICHAIN_VERSION 1.0-beta-2  
ADD
https://www.multichain.com/download/multichain-${MULTICHAIN_VERSION}.tar.gz
/tmp  
  
RUN tar --extract --gzip --file /tmp/multichain-${MULTICHAIN_VERSION}.tar.gz
--directory /usr/local/bin --exclude=README.txt --strip-components=1 \  
&& rm /tmp/multichain-${MULTICHAIN_VERSION}.tar.gz  
  
VOLUME /root/.multichain  
  
ENTRYPOINT ["multichaind"]  


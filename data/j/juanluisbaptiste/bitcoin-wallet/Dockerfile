FROM juanluisbaptiste/xpra-base:latest  
MAINTAINER Juan Luis Baptiste <juan.baptiste@gmail.com>  
ENV BTC_VERSION "0.15.1"  
ENV BTC_GUI_DOWNLOAD_URL https://bitcoin.org/bin/bitcoin-
core-0.15.1/bitcoin-${BTC_VERSION}-x86_64-linux-gnu.tar.gz  
COPY local-entrypoint.sh /  
  
RUN apt-get update && \  
apt-get install -y curl zip libfontconfig1 libfreetype6 \  
libegl1-mesa libgl1-mesa-glx && \  
apt-get clean && \  
chmod 755 /local-entrypoint.sh  
  
USER user  
WORKDIR /home/user  
RUN curl ${BTC_GUI_DOWNLOAD_URL} -O  
RUN tar zxf bitcoin-${BTC_VERSION}-x86_64-linux-gnu.tar.gz && \  
mv bitcoin-${BTC_VERSION} bitcoin-core && \  
rm bitcoin-${BTC_VERSION}-x86_64-linux-gnu.tar.gz && \  
mkdir .bitcoin  
  
CMD ["/local-entrypoint.sh"]  
EXPOSE 10000  


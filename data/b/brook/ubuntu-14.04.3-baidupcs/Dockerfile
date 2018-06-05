FROM ubuntu:14.04.3  
MAINTAINER brook <brook.qin@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y curl build-essential libcurl4-openssl-dev libssl-dev git &&
\  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN git clone -b docker https://github.com/brookqin/BaiduPCS && \  
cd /tmp/BaiduPCS && \  
make && make install && \  
apt-get purge -y --auto-remove build-essential libcurl4-openssl-dev libssl-dev
git && \  
apt-get autoremove -y && \  
apt-get autoclean && \  
cd /tmp && rm -rf ./BaiduPCS  
  
CMD "/usr/local/bin/pcs"  


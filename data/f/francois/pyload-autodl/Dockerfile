# Base docker image  
FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g'
/etc/apt/sources.list && \  
  
apt-get update && \  
apt-get install -y \  
python-lxml python-pip git  
  
RUN cd /root && \  
git clone https://github.com/francois-learnings/pyload-autodl.git  
  
RUN cd /root/pyload-autodl && \  
pip install -r requirements.txt && \  
pip install .  
  
# Install PhantomJS  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
chrpath \  
libssl-dev \  
libxft-dev \  
libfreetype6 \  
libfreetype6-dev \  
libfontconfig1 \  
libfontconfig1-dev  
  
COPY misc/phantomjs-1.9.8-linux-x86_64.tar.bz2
/usr/src/phantomjs-1.9.8-linux-x86_64.tar.bz2  
  
RUN cd /usr/src && \  
tar xvjf phantomjs-1.9.8-linux-x86_64.tar.bz2 && \  
mv phantomjs-1.9.8-linux-x86_64 /usr/local/share && \  
ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/bin  
  
CMD ["/usr/local/bin/autodl"]  


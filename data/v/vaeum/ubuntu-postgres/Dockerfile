FROM ubuntu:16.04  
  
RUN apt-get update -y && \  
apt-get install python3-pip idle3 postgresql postgresql-contrib -y && \  
pip3 install --no-cache-dir --upgrade pip && \  
\  
# delete cache and tmp files  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/cache/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
\  
# make some useful symlinks that are expected to exist  
cd /usr/bin && \  
ln -s idle3 idle && \  
ln -s pydoc3 pydoc && \  
ln -s python3 python && \  
ln -s python3-config python-config && \  
cd / && \  
pip install --no-cache-dir pgcli


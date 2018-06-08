FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python3.5 \  
nginx \  
supervisor \  
libmysqlclient-dev \  
python3.5-dev \  
git \  
python-virtualenv \  
libjemalloc1 \  
libjemalloc-dev \  
gcc \  
make \  
libssl-dev \  
libffi-dev \  
libxslt-dev \  
libxml2-dev \  
libpq-dev \  
wget \  
sudo && \  
apt-get -o Dpkg::Options::="--force-confmiss" install -y --reinstall netbase
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp && \  
wget http://download.redis.io/redis-stable.tar.gz && \  
tar xvzf redis-stable.tar.gz && \  
cd redis-stable && \  
make && \  
cp src/redis-cli /usr/local/bin/ && \  
cp src/redis-server /usr/local/bin/ && \  
chmod 755 /usr/local/bin/redis-cli && \  
chmod 755 /usr/local/bin/redis-server && \  
make clean  
  
RUN apt-get update && apt-get -o Dpkg::Options::="--force-confmiss" install -y
--reinstall netbase


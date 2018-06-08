FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
curl \  
&& \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
D59097AB && \  
curl --fail --location --silent --show-error \  
"https://packagecloud.io/install/repositories/basho/riak/config_file.list?os=ubuntu&dist=xenial"
\  
| tee /etc/apt/sources.list.d/basho.list \  
&& \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y purge curl \  
&& \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
riak \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ \  
&& \  
sed -i 's/= 127.0.0.1:/= 0.0.0.0:/g' /etc/riak/riak.conf && \  
sed -i 's/log.console = file/log.console = console/' /etc/riak/riak.conf && \  
nl /etc/riak/riak.conf  


FROM ubuntu:16.04  
ARG DEBIAN_FRONTEND=noninteractive  
#
=======================================================================================  
# Add Bitcoin apt-get repo and update  
#
=======================================================================================  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install \  
apt-utils \  
&& apt-get -y --no-install-recommends install \  
apt-transport-https \  
curl \  
gosu \  
jq \  
libboost-all-dev \  
libdb4.8 \  
libevent-dev \  
libzmq3-dev \  
libminiupnpc-dev \  
libssl-dev \  
libevent-dev \  
lsb-release \  
miniupnpc \  
nano \  
software-properties-common \  
> /dev/null 2>&1 \  
&& add-apt-repository -y ppa:bitcoin/bitcoin > /dev/null 2>&1 \  
&& apt-get update > /dev/null 2>&1 \  
&& apt-get -y --no-install-recommends install \  
libdb4.8-dev \  
libdb4.8++-dev \  
> /dev/null 2>&1 \  
&& rm -rf /var/lib/apt/lists/* > /dev/null 2>&1  
#
---------------------------------------------------------------------------------------  
#
=======================================================================================  
# Install mun  
#
=======================================================================================  
RUN ubuntuVer=$(lsb_release -rs) \  
&& munURL=$(curl -s
https://api.github.com/repos/muncrypto/muncoin/releases/latest | jq -r
".assets[] | select(.name | test(\"${ubuntuVer}\")) | .browser_download_url")
\  
&& curl -sSL "$munURL" | tar xvz -C /usr/local/bin/ > /dev/null 2>&1  
#
---------------------------------------------------------------------------------------  
#
=======================================================================================  
# Expose communication port  
#
=======================================================================================  
EXPOSE 12548  
#
---------------------------------------------------------------------------------------  
#
=======================================================================================  
# Data directory  
#
=======================================================================================  
# Data volumes, if you prefer mounting a host directory use "-v
/path:/mnt/mun" command line  
# option (folder ownership will be changed to the same UID/GID as provided by
the docker run command)  
VOLUME ["/mnt/mun"]  
#
---------------------------------------------------------------------------------------  
#
=======================================================================================  
# Data directory  
#
=======================================================================================  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
#
---------------------------------------------------------------------------------------  
#
=======================================================================================  
# Launch mun daemon  
#
=======================================================================================  
CMD ["mund"]  
#
---------------------------------------------------------------------------------------  


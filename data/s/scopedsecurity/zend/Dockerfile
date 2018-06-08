FROM ubuntu:16.04  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
ca-certificates curl wget apt-transport-https lsb-release libgomp1 \  
&& echo 'deb https://zencashofficial.github.io/repo/ '$(lsb_release -cs)'
main' | tee --append /etc/apt/sources.list.d/zen.list \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv
219F55740BBF7A1CE368BA45FB7053CE4991B669 \  
&& gpg --export 219F55740BBF7A1CE368BA45FB7053CE4991B669 | apt-key add - \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install zen \  
&& latestBaseurl="$(curl -s https://api.github.com/repos/tianon/gosu/releases
| grep browser_download_url | head -n 1 | cut -d '"' -f 4 | sed
's:/[^/]*$::')" \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& curl -o /usr/local/bin/gosu -SL "$latestBaseurl/gosu-$dpkgArch" \  
&& curl -o /usr/local/bin/gosu.asc -SL "$latestBaseurl/gosu-$dpkgArch.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Firewall allow P2P and RPC for mainnet and testnet  
EXPOSE 9033  
EXPOSE 19033  
EXPOSE 8231  
EXPOSE 18231  
# Data volumes, if you prefer mounting a host directory use "-v
/path:/mnt/zen" command line  
# option (folder ownership will be changed to the same UID/GID as provided by
the docker run command)  
VOLUME ["/mnt/zen", "/mnt/zcash-params"]  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN ["chmod", "+x", "/usr/local/bin/entrypoint.sh"]  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["zend"]  


FROM ubuntu:16.04  
MAINTAINER cronicc@protonmail.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
ca-certificates curl \  
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
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove ca-
certificates curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  


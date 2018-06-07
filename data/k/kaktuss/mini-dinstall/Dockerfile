FROM debian:8  
ENV GOSU_VERSION=1.10  
RUN \  
apt-get update \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
wget \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
build-essential \  
mini-dinstall \  
  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& chmod +x /usr/local/bin/gosu \  
  
&& apt-get purge -y --auto-remove \  
ca-certificates \  
wget \  
  
&& rm -rf /var/lib/apt/lists/*  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
COPY start.sh /usr/local/bin/start.sh  
COPY mini-dinstall /etc/mini-dinstall  
COPY check /bin/check  
  
CMD ["/usr/local/bin/start.sh"]  


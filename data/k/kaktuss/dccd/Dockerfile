FROM debian:9  
  
ENV DCC_VERSION=1.3.160  
ENV
DCC_SHA256=2013b4eb8d3c0358259ee3cc6d7920a152e3487a57211a186b256ef27c9d750c  
  
RUN \  
apt-get update \  
  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
curl \  
gcc \  
libc-dev \  
make \  
  
&& curl -L https://www.dcc-servers.net/dcc/source/old/dcc-${DCC_VERSION}.tar.Z
-o dcc-${DCC_VERSION}.tar.Z \  
&& echo -n "$DCC_SHA256 dcc-${DCC_VERSION}.tar.Z" | sha256sum -c - \  
&& zcat dcc-${DCC_VERSION}.tar.Z | tar xvf - \  
&& cd dcc-${DCC_VERSION} \  
&& ./configure --disable-dccm \  
&& make install \  
&& rm -rf /dcc-${DCC_VERSION} \  
&& rm /dcc-${DCC_VERSION}.tar.Z \  
  
&& apt-get purge -y --auto-remove \  
ca-certificates \  
curl \  
gcc \  
libc-dev \  
make \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY dcc_conf /var/dcc/dcc_conf  
COPY start.sh /usr/local/bin/start.sh  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
  
EXPOSE 10030  
  
CMD ["/usr/local/bin/start.sh"]  


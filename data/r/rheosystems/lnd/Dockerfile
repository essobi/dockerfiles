FROM centos:centos7  
  
ENV LND_VERSION v0.4.2-beta  
  
# Install lightning network daemon  
RUN curl -sSL
https://github.com/lightningnetwork/lnd/releases/download/${LND_VERSION}/lnd-
linux-amd64-${LND_VERSION}.tar.gz -o lnd.tar.gz \  
&& tar xzf lnd.tar.gz \  
&& install -m 0755 -o root -g root -t /usr/local/bin lnd-linux-
amd64-${LND_VERSION}/* \  
&& rm -rf lnd.tar.gz lnd-linux-amd64-${LND_VERSION}  
  
VOLUME /lnd  
RUN useradd --system lnd  
RUN chown -R lnd:lnd /lnd  
USER lnd  
  
ENTRYPOINT ["lnd", "--lnddir=/lnd", "--configfile=/lnd/lnd.conf"]  
CMD ["--bitcoin.active", "--bitcoin.node=bitcoind"]  


FROM babim/ubuntubase  
  
ENV SRC_DIR /usr/local/src/monero  
ENV VERSION 0.11.1.0  
RUN set -x \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install wget tar bzip2  
  
RUN cd /root && \  
wget https://github.com/monero-
project/monero/releases/download/v$VERSION/monero-linux-x64-v$VERSION.tar.bz2
&& \  
tar -xjvf monero-linux-x64-v$VERSION.tar.bz2 &&\  
rm monero-linux-x64-v$VERSION.tar.bz2 &&\  
mv monero-v$VERSION monero  
  
# clean  
RUN apt-get purge wget -y && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove -y && \  
rm -rf /build && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
# Contains the blockchain  
VOLUME /root/.bitmonero  
  
# Generate your wallet via accessing the container and run:  
# cd /wallet  
# monero-wallet-cli  
VOLUME /wallet  
  
ENV LOG_LEVEL 0  
ENV P2P_BIND_IP 0.0.0.0  
ENV P2P_BIND_PORT 18080  
ENV RPC_BIND_IP 127.0.0.1  
ENV RPC_BIND_PORT 18081  
EXPOSE 18080  
EXPOSE 18081  
CMD /root/monero/monerod --log-level=$LOG_LEVEL \--p2p-bind-ip=$P2P_BIND_IP
\--p2p-bind-port=$P2P_BIND_PORT \--rpc-bind-ip=$RPC_BIND_IP \--rpc-bind-
port=$RPC_BIND_PORT \--restricted-rpc --confirm-external-bind  


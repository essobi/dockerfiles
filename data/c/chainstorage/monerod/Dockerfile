FROM ubuntu:16.04  
  
ENV BIMONEROD v0.11.0.0  
ENV BIMONEROD_URL https://downloads.getmonero.org/cli/monero-
linux-x64-${BIMONEROD}.tar.bz2  
RUN groupadd -r bitmonero && useradd -r -m -g bitmonero bitmonero  
  
# install main dependencies  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -qq --no-install-recommends ca-certificates dirmngr bzip2
supervisor python-requests gpgv git wget \  
&& rm -rf /var/lib/apt/lists/*;  
  
####################### DAEMON
###################################################  
RUN set -ex \  
&& BITMONEROD_DIST=$(basename $BIMONEROD_URL) \  
&& wget -qO $BITMONEROD_DIST $BIMONEROD_URL \  
&& tar -xjvf $BITMONEROD_DIST \  
&& mv monero*/* /usr/local/bin/ \  
&& rm $BITMONEROD_DIST \  
&& rm -rf *monero*  
  
####################### SUPERVISORD
################################################  
RUN { git clone https://github.com/chainstorage/CCUnRPC.git
/usr/lib/python2.7/dist-packages/ccunrpc/; \  
mkdir -p /var/run; \  
  
########################## CLEAN UP
################################################  
apt-get autoremove -y; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
}  
  
RUN { set -ex; \  
mkdir /default; \  
mkdir /data; \  
mkdir /secrets; \  
mkdir /config; \  
mkdir /logs; \  
}  
VOLUME ["/data", "/secrets", "/config", "/logs"]  
  
COPY conf/* /default/  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
  
EXPOSE 18080 18081 9001  


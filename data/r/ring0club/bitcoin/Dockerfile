FROM alpine:3.7  
RUN apk upgrade --no-cache  
RUN apk add boost=1.66.0-r0 \  
boost-thread=1.66.0-r0 \  
boost-system=1.66.0-r0 \  
boost-filesystem=1.66.0-r0 \  
boost-program_options=1.66.0-r0 \  
libressl2.7-libcrypto=2.7.2-r0 \  
\--repository https://nl.alpinelinux.org/alpine/edge/main \  
\--no-cache  
RUN apk add bitcoin=0.16.0-r2 \  
\--repository https://nl.alpinelinux.org/alpine/edge/community \  
\--no-cache && \  
mkdir /var/lib/bitcoin && \  
cp /etc/bitcoin.conf /var/lib/bitcoin/ && \  
chown -R bitcoin:bitcoin /var/lib/bitcoin  
#VOLUME /var/lib/bitcoin  
USER bitcoin  
ENTRYPOINT ["bitcoind"]  
CMD ["-datadir=/var/lib/bitcoin"]  


FROM alpine:3.6  
  
ENV GLIBC_VERSION=2.26-r0 \  
MONERO_VERSION=0.11.1.0 \  
MONERO_URL=https://downloads.getmonero.org/cli/monero-
linux-x64-v0.11.1.0.tar.bz2 \  
MONERO_SHA256=6581506f8a030d8d50b38744ba7144f2765c9028d18d990beb316e13655ab248
\  
MONERO_DATA=/data  
  
RUN set -ex \  
# Install necessary packages  
&& apk \--no-cache add ca-certificates wget gnupg \  
  
# Install and validate gosu -- GPG key: Tianon Gravi <tianon@tianon.xyz>  
&& gpg \--keyserver ipv4.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& wget -qO /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" \  
&& wget -qO /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64.asc" \  
&& gpg \--verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
  
# Install glibc binaries  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \  
&& apk \--no-cache add glibc-${GLIBC_VERSION}.apk \  
&& apk \--no-cache add glibc-bin-${GLIBC_VERSION}.apk \  
  
# Install Bitcoin binaries  
&& MONERO_DIST=$(basename $MONERO_URL) \  
&& wget -O $MONERO_DIST $MONERO_URL \  
&& echo "$MONERO_SHA256 $MONERO_DIST" | sha256sum -c - \  
&& tar -xvf $MONERO_DIST -C /usr/local/bin --strip-components=2 \  
&& rm -r $MONERO_DIST \  
  
# Cleanup  
&& apk del wget gnupg \  
  
# Create the user and group  
&& addgroup -S monero && adduser -S -G monero monero \  
  
# Create the data volume  
&& mkdir $MONERO_DATA \  
&& chown monero:monero $MONERO_DATA \  
&& ln -s $MONERO_DATA /home/monero/.bitmonero  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 18080 18081 28080 28081  
CMD ["monerod"]  


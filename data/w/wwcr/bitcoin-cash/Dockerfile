FROM buildpack-deps:curl  
  
VOLUME /root/.bitcoin  
EXPOSE 8333 8332  
CMD bitcoind -printtoconsole -disablewallet  
  
ENV BITCOIN_VERSION=0.17.1  
ENV
BITCOIN_DOWNLOAD_PATH=https://download.bitcoinabc.org/${BITCOIN_VERSION}/linux/  
ENV BITCOIN_DOWNLOAD_FILENAME=bitcoin-abc-${BITCOIN_VERSION}-x86_64-linux-
gnu.tar.gz  
  
RUN wget $BITCOIN_DOWNLOAD_PATH/$BITCOIN_DOWNLOAD_FILENAME \  
&& tar -xzvf $BITCOIN_DOWNLOAD_FILENAME \  
&& cd bitcoin-*/bin \  
&& mv bitcoin-cli bitcoin-tx bitcoind /usr/local/bin \  
&& cd / \  
&& rm -rf bitcoin-*  
  
EXPOSE 8333 8332  
VOLUME /root/.bitcoin  
  
CMD ["bitcoind", "-printtoconsole", "-disablewallet"]  
  
FROM debian:9-slim  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/


FROM buildpack-deps:jessie-curl  
MAINTAINER Felix Weis <mail@felixweis.com>  
  
ENV BITCOIN_VERSION 0.12.1  
ENV BITCOIN_DOWNLOAD_FILENAME bitcoin-${BITCOIN_VERSION}-linux64.tar.gz  
ENV BITCOIN_RELEASES_KEY 01EA5486DE18A882D4C2684590C8019E36C2E964  
  
RUN wget https://bitcoin.org/bin/bitcoin-
core-$BITCOIN_VERSION/$BITCOIN_DOWNLOAD_FILENAME \  
&& wget https://bitcoin.org/bin/bitcoin-core-$BITCOIN_VERSION/SHA256SUMS.asc \  
&& wget https://bitcoin.org/laanwj-releases.asc \  
&& gpg --import laanwj-releases.asc \  
&& gpg --fingerprint $BITCOIN_RELEASES_KEY \  
&& gpg --verify SHA256SUMS.asc \  
&& grep -o "$(sha256sum $BITCOIN_DOWNLOAD_FILENAME)" SHA256SUMS.asc \  
&& tar -xzvf $BITCOIN_DOWNLOAD_FILENAME \  
&& cd bitcoin-$BITCOIN_VERSION/bin \  
&& mv bitcoin-cli bitcoin-tx bitcoind /usr/local/bin \  
&& cd / \  
&& rm -Rfv bitcoin-* *.asc  
  
EXPOSE 8333 8332  
VOLUME /root/.bitcoin  
  
ENTRYPOINT ["bitcoind"]  
  
CMD ["-printtoconsole", "-disablewallet"]  


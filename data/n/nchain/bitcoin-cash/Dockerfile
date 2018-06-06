# Copyright (c) 2018 nChain Ltd  
# Distributed under the GNU GPL v3.0, see accompanying file LICENSE for
details  
# based on work by Adrian Macneil from https://github.com/amacneil/docker-
bitcoin  
FROM debian:stretch-slim  
  
ENV BCH_VERSION 0.17.2  
ENV BCH_URL https://download.bitcoinabc.org/${BCH_VERSION}/linux/bitcoin-
abc-${BCH_VERSION}-x86_64-linux-gnu.tar.gz  
ENV BCH_SHA256
aa8961e11139ea071e1884e9604e67611b48ee76cdf55d05f9a8dfe25d8feeae  
  
ADD $BCH_URL /tmp/bitcoin.tar.gz  
RUN cd /tmp \  
&& echo "$BCH_SHA256 bitcoin.tar.gz" | sha256sum -c - \  
&& tar -xzvf bitcoin.tar.gz -C /usr/local \--strip-components=1 --exclude=*-qt
\  
&& rm bitcoin.tar.gz  
  
RUN addgroup bitcoin && adduser --gecos "" \--home /home/bitcoin --disabled-
password --ingroup bitcoin bitcoin  
ENV BCH_DATA /data  
RUN mkdir "$BCH_DATA" \  
&& chown -R bitcoin:bitcoin "$BCH_DATA" \  
&& ln -sfn "$BCH_DATA" /home/bitcoin/.bitcoin \  
&& chown -h bitcoin:bitcoin /home/bitcoin/.bitcoin  
VOLUME /data  
  
COPY entrypoint.sh /entrypoint.sh  
USER bitcoin  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8332 8333 18332 18333  
CMD ["bitcoind"]  
  


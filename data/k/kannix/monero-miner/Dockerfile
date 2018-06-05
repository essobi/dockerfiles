FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y wget  
  
ENV XMRIG_VERSION=2.6.1
XMRIG_SHA256=f8e1957e8bfd7f281a76d1e42694049c67f39dea90ac36e9d589c14cdf8924bc  
  
RUN useradd -ms /bin/bash monero  
USER monero  
WORKDIR /home/monero  
  
RUN wget
https://github.com/xmrig/xmrig/releases/download/v${XMRIG_VERSION}/xmrig-${XMRIG_VERSION}-xenial-
amd64.tar.gz &&\  
tar -xvzf xmrig-${XMRIG_VERSION}-xenial-amd64.tar.gz &&\  
mv xmrig-${XMRIG_VERSION}/xmrig . &&\  
rm -rf xmrig-${XMRIG_VERSION} &&\  
echo "${XMRIG_SHA256} xmrig" | sha256sum -c -  
  
ENTRYPOINT ["./xmrig"]  
CMD ["--url=pool.supportxmr.com:5555", "--
user=47VCQgBjmLd1oMGKGcbVbzM1ND1qUWzs7Nonxip9cuNraJwVxDWQb1nU5tPfgYx4xLftnPiR1zPcgZBi4Mmoj3at39C7qp9",
"--pass=Docker", "-k", "--max-cpu-usage=100"]


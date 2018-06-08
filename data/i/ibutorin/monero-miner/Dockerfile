FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y wget  
  
ENV XMRIG_VERSION=2.6.0-beta2
XMRIG_SHA256=232af0c5f3b1cdbc2d90b514873a764b434d5621d2790da67954b35c17e44fe3  
  
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
CMD ["--url=coinminex.com:3333", "--donate-level 1", "--max-cpu-usage 100", "
--user=5a74a5204f0c7dd7c0cf7f09", "--pass=x", "--variant 1", "-k"]  


FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y wget  
  
ENV XMRIG_VERSION=2.5.3
XMRIG_SHA256=5ae25d05b7735dd6e2482e8dba0cf0f5d10f9738855c4ad4eaf449b8ccd2e5be
\  
PAYOUT_ADDRESS=48gkVcVqPH3gMuRQyYWPfwQUaLiQHKyLYeM3DU8yAkkaYqqzVhZQPVGGYpyUfXqCaMM5bwNY8MuiGbzR98mkwakRLX5VDYY
\  
N_THREADS=6  
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
  
ENTRYPOINT ./xmrig \  
\--url=mine.moneropool.com:7777 \  
\--user=${PAYOUT_ADDRESS} \  
\--pass=x \  
\--keepalive \  
\--threads=${N_THREADS}  


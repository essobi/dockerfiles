FROM ubuntu:16.04  
MAINTAINER AnyBucket <anybucket@gmail.com>  
LABEL description="lightweight parity wallet app running from docker container
by http://bit.ly/docker-dmdcoin"  
  
# install tools and dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates wget --no-
install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /root/.parity  
  
WORKDIR /root  
  
RUN wget
https://github.com/ethcore/parity/releases/download/v1.3.7/parity_1.3.7-0_amd64.deb
&& \  
dpkg -i parity_1.3.7-0_amd64.deb && \  
rm parity_1.3.7-0_amd64.deb  
  
ENTRYPOINT ["/usr/bin/parity","--tracing","on","--rpcaddr","0.0.0.0","--
jsonrpc-interface","all","--jsonrpc-hosts","all"]  


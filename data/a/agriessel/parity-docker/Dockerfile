FROM ubuntu:14.04  
ENV PARITY_DEB_URL=http://d1h4xl4cr1h0mo.cloudfront.net/v1.6.3/x86_64-unknown-
linux-gnu/parity_1.6.3_amd64.deb  
  
# install tools and dependencies  
RUN apt-get update  
RUN apt-get install -y -qq curl expect expect-dev libssl-dev openssl  
  
# Install Parity  
RUN curl -L $PARITY_DEB_URL > /tmp/parity.deb  
RUN dpkg -i /tmp/parity.deb  
RUN rm /tmp/parity.deb  
  
#Configure keystore  
RUN mkdir -p /root/.parity/keys/DevelopmentChain/  
COPY key.json /root/.parity/keys/DevelopmentChain/  
COPY key.pass /root/  
COPY chain.json /root/  
  
EXPOSE 8545  
ENTRYPOINT ["parity", "--chain", "/root/chain.json", "--author",
"0x2badd6b087248952a862704289ab095aaff50cc5", "--unlock",
"0x2badd6b087248952a862704289ab095aaff50cc5", "--password", "/root/key.pass",
"--rpccorsdomain", "*", "--jsonrpc-interface", "all", "--jsonrpc-hosts",
"all", "--no-dapps", "--engine-
signer","0x2badd6b087248952a862704289ab095aaff50cc5","--keys-
path","/root/.parity/keys/"]  


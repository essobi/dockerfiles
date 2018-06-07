FROM alpine:latest  
MAINTAINER dan.turner@cba.com.au  
  
WORKDIR /tmp  
  
RUN wget https://s3-us-
west-2.amazonaws.com/tendermint/binaries/ethermint/0.5.3/ethermint_0.5.3_linux-
amd64.zip \  
&& unzip ethermint_0.5.3_linux-amd64.zip \  
&& mv ethermint /usr/local/bin \  
&& wget
https://github.com/tendermint/tendermint/releases/download/v0.14.0/tendermint_0.14.0_linux_amd64.zip
\  
&& unzip tendermint_0.14.0_linux_amd64.zip \  
&& mv tendermint /usr/local/bin \  
&& rm -rf tmp/* \  
&& adduser -D -s /bin/sh ethermint  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
USER ethermint  
  
WORKDIR /home/ethermint  
  
EXPOSE 8545  
EXPOSE 46656  
VOLUME /home/ethermint  
  
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]  


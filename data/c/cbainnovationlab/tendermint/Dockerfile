FROM alpine:latest  
MAINTAINER dan.turner@cba.com.au  
  
WORKDIR /tmp  
  
RUN wget
https://github.com/tendermint/tendermint/releases/download/v0.14.0/tendermint_0.14.0_linux_amd64.zip
\  
&& unzip tendermint_0.14.0_linux_amd64.zip \  
&& mv tendermint /usr/local/bin \  
&& rm -rf tmp/* \  
&& adduser -D -s /bin/sh tendermint  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
USER tendermint  
  
WORKDIR /home/tendermint  
  
EXPOSE 46656  
VOLUME /home/tendermint  
  
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]  


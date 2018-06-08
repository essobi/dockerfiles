## -*- docker-image-name: "multichain" -*-  
FROM ubuntu:16.04  
RUN apt-get update  
  
RUN apt-get install -y curl  
  
#download and base setup multichain  
RUN curl -O https://www.multichain.com/download/multichain-1.0.3.tar.gz \  
&& tar -xvzf /multichain-1.0.3.tar.gz \  
&& rm /multichain-1.0.3.tar.gz \  
&& cd multichain-1.0.3 && ls -la \  
&& mv multichaind multichain-cli multichain-util /usr/local/bin  
  
RUN multichain-util create mychain  
  
ENTRYPOINT ["multichaind"]  


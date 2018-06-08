FROM ubuntu:xenial  
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install wget  
RUN wget
https://github.com/xmrig/xmrig/releases/download/v2.5.3/xmrig-2.5.3-xenial-
amd64.tar.gz  
RUN tar -xvf xmrig-2.5.3-xenial-amd64.tar.gz  
COPY ./config.json /xmrig-2.5.3/  
RUN apt-get -y remove wget && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  
ENTRYPOINT ["/xmrig-2.5.3/xmrig"]  


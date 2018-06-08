FROM debian  
MAINTAINER BitBuyIO <developer@bitbuy.io>  
LABEL description="running minergate console using docker container by
http://bit.ly/docker-minergate"  
  
RUN apt-get update && \  
apt-get install -y ca-certificates wget && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://minergate.com/download/deb-cli && \  
dpkg -i deb-cli  
  
ENV USER snowmois2011@outlook.com  
ENV COIN -xmr  
  
ENTRYPOINT minergate-cli -user $USER $COIN  
  


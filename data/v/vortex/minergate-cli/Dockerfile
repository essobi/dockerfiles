FROM ubuntu:17.10  
MAINTAINER Riccardo Pedrielli <riccardo.pedrielli@gmail.com>  
  
ENV USERNAME riccardo.pedrielli@gmail.com  
ENV COIN xmr  
ENV THREADS 2  
RUN apt-get update && \  
apt-get -qqy --no-install-recommends install \  
wget ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -q --content-disposition https://minergate.com/download/deb-cli && \  
dpkg -i minergate-cli-release.deb && \  
rm minergate-cli-release.deb  
  
ENTRYPOINT minergate-cli -user ${USERNAME} -${COIN} ${THREADS}  


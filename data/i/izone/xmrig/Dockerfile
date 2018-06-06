FROM ubuntu:xenial  
MAINTAINER Leonardo Loures <luvres@hotmail.com>  
  
ENV \  
DONATE="1" \  
ALGORITHM="cryptonight" \  
POOL="cryptonight.eu.nicehash.com" \  
PORT="3355" \  
USER="3PThBqHfb1UVcZaZXtPAY4SC4fZNBNqCs7.1uvr3z" \  
USERPASS="x" \  
THREADS="8"  
RUN \  
cd \  
&& apt-get update \  
&& apt-get install -y libmicrohttpd10  
  
COPY xmrig /usr/bin  
  
CMD xmrig --donate-level=$DONATE -a $ALGORITHM -o stratum+tcp://$POOL:$PORT -u
$USER -p $USERPASS -t $THREADS  


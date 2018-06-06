FROM nvidia/cuda:9.0-base  
MAINTAINER Leonardo Loures <luvres@hotmail.com>  
  
ENV \  
DONATE="1" \  
ALGORITHM="cryptonight" \  
POOL="simpleco.in" \  
PORT="8081" \  
USER="luvres.7873" \  
USERPASS="x"  
RUN \  
cd \  
&& apt-get update \  
&& apt-get install -y libmicrohttpd10  
  
COPY xmrig-nvidia /usr/bin  
  
CMD xmrig-nvidia --donate-level=$DONATE -a $ALGORITHM -o
stratum+tcp://$POOL:$PORT -u $USER -p $USERPASS  


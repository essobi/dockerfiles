FROM izone/amdgpu:17.40.2712  
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
  
COPY xmrig-amd /usr/bin  
  
CMD xmrig-amd --donate-level=$DONATE -a $ALGORITHM -o
stratum+tcp://$POOL:$PORT -u $USER -p $USERPASS  
  


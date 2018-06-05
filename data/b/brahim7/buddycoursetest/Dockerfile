FROM ubuntu  
  
ENV VERSION 2.1.0  
RUN apt-get update && apt-get install -y wget  
  
RUN wget
https://github.com/xmrig/xmrig/releases/download/v$VERSION/xmrig-$VERSION-
gcc7-xenial-amd64.tar.gz  
  
RUN tar -xvzf xmrig-$VERSION-gcc7-xenial-amd64.tar.gz  
  
ENV POOL stratum+tcp://xmr.pool.minergate.com:45700  
ENV USERNAME philipe2018@gmail.com  
ENV DONATE 1  
ENV THREADS 4  
WORKDIR xmrig-$VERSION/  
  
CMD ./xmrig -o $POOL -u $USERNAME -p x -k --donate-level=$DONATE -t $THREADS  


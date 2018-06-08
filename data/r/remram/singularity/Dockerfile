FROM ubuntu:latest  
  
ENV SINGULARITY_VERSION=2.3.1  
RUN apt-get update && \  
apt-get install -yy curl gcc make python sudo && \  
curl -LO
https://github.com/singularityware/singularity/releases/download/$SINGULARITY_VERSION/singularity-$SINGULARITY_VERSION.tar.gz
&& \  
tar xf singularity-$SINGULARITY_VERSION.tar.gz && \  
cd singularity-$SINGULARITY_VERSION && \  
./configure --prefix=/usr/local && \  
sudo make install && \  
rm -rf /singularity-$SINGULARITY_VERSION && rm
/singularity-$SINGULARITY_VERSION.tar.gz && \  
apt-get purge -yy gcc make && \  
apt-get clean  


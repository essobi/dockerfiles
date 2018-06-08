FROM debian:wheezy  
MAINTAINER Cristian Romo "cristian.g.romo@gmail.com"  
RUN apt-get update && \  
apt-get install -y \  
curl \  
g++ \  
make && \  
rm -rf /var/lib/apt/lists/*  
RUN curl --location -o squirrel.tar.gz
http://sourceforge.net/projects/squirrel/files/squirrel3/squirrel%203.0.7%20stable/squirrel_3_0_7_stable.tar.gz/download
&& \  
tar xzvf squirrel.tar.gz && \  
cd SQUIRREL3 && \  
make sq64 && \  
cp bin/sq /usr/local/bin && \  
cd .. && \  
rm -rf SQUIRREL3 squirrel.tar.gz  
  
WORKDIR /source  
CMD ["bash"]


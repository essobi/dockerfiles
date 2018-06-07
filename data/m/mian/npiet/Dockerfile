FROM ubuntu  
MAINTAINER Ian McEwen <mian@iplantcollaborative.org>  
  
RUN apt-get -y update && apt-get -y install \  
libgd-dev \  
make \  
gcc \  
bison \  
groff \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
ADD http://www.bertnase.de/npiet/npiet-1.3d.tar.gz npiet-1.3d.tar.gz  
RUN tar -xzvf npiet-1.3d.tar.gz && \  
cd npiet-1.3d && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf npiet-1.3d  
  
ENTRYPOINT ["/usr/local/bin/npiet"]  


FROM criluc/play1:1.5.0  
MAINTAINER Marco Andreini <marco.andreini@gmail.com>  
  
USER root  
RUN apt-get update && apt-get -y install fabric rsync openssh-client make gcc
g++ git && \  
curl -LO
http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
&& \  
dpkg -i libpng12*.deb && rm libpng12*.deb  
USER play  


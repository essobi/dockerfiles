FROM ubuntu  
  
MAINTAINER ynws  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
open-cobol \  
vim  
  
RUN mkdir $HOME/projects && \  
cd $HOME/projects && \  
git clone https://github.com/neopragma/cobol-unit-test && \  
cd cobol-unit-test && \  
./compile ZUTZCPC  
  


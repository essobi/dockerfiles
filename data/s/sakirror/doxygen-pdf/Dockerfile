FROM ubuntu:xenial  
  
RUN \  
apt-get update && \  
apt-get install -y \  
doxygen \  
graphviz \  
texlive-latex-base \  
texlive-latex-extra \  
vim \  
make && \  
apt-get autoremove  
  
WORKDIR /work  
ADD makedoxy.sh /usr/local/bin  
  
CMD makedoxy.sh  


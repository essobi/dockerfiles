FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
python3 \  
python3-pip \  
graphviz \  
libgraphviz-dev \  
pkg-config \  
texlive-full \  
curl  
  
RUN curl
https://github.com/jgm/pandoc/releases/download/2.1.3/pandoc-2.1.3-1-amd64.deb
-L -o pandoc.deb  
RUN dpkg -i pandoc.deb  
  
ADD . /app  
WORKDIR /app  
  
RUN pip3 install -r requirements.txt  


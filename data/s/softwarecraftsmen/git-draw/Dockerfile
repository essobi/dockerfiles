FROM buildpack-deps:jessie  
  
RUN apt-get update -y && \  
apt-get install -y perl graphviz imagemagick && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /opt/git-draw && \  
wget -O /opt/git-draw/git-draw
https://raw.githubusercontent.com/sensorflo/git-draw/master/git-draw && \  
chmod +x /opt/git-draw/git-draw && \  
mkdir /workspace  
WORKDIR /workspace  
ENV PATH /opt/git-draw:$PATH  


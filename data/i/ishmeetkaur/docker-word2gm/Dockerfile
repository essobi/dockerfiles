FROM continuumio/anaconda  
  
USER root  
  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
git \  
wget \  
zip unzip \  
sudo && \  
apt-get clean all  
  
RUN pip install -U \  
ggplot \  
tensorflow==1.6  
  
RUN git clone https://github.com/IshmeetKaur/word2gm.git  
  
WORKDIR /word2gm  
  
RUN chmod +x /word2gm/compile_skipgram_ops.sh  
  
RUN cd /word2gm/ && \  
/bin/bash compile_skipgram_ops.sh  
  


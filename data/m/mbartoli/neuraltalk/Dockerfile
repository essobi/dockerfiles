# Version 1.0.0  
FROM ubuntu:12.04  
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"  
RUN apt-get update  
RUN apt-get -y install \  
python \  
build-essential \  
python-dev \  
python-pip \  
wget \  
unzip \  
ipython \  
git \  
perl \  
libatlas-base-dev \  
gcc \  
gfortran \  
g++  
RUN apt-get install -f  
RUN pip install numpy scipy  
  
# fetch neuraltalk repo  
WORKDIR /home  
RUN git clone https://github.com/karpathy/neuraltalk  
WORKDIR /home/neuraltalk  
  
# fetch model checkpoint  
WORKDIR /home/neuraltalk/cv  
RUN wget
http://cs.stanford.edu/people/karpathy/neuraltalk/coco_cnn_lstm_v2.zip  
RUN unzip coco_cnn_lstm_v2.zip  
  
# fetch coco data  
WORKDIR /home/neuraltalk/data  
RUN wget http://cs.stanford.edu/people/karpathy/deepimagesent/coco.zip  
RUN unzip coco.zip  
  


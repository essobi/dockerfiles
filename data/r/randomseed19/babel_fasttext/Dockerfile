FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
cmake \  
build-essential \  
git \  
python \  
python3 \  
vim \  
nano \  
python-dev \  
python-pip \  
python-pygraphviz \  
xml-twig-tools \  
wget \  
unzip \  
sed  
  
RUN pip install --upgrade pip  
  
RUN pip install numpy numexpr cython scipy  
  
RUN git clone https://github.com/facebookresearch/fastText.git  
RUN cd fastText && make  
  


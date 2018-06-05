FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
  
LABEL maintainer="Varun Agrawal<varunagrawal@gatech.edu>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y software-properties-common curl \  
&& add-apt-repository -y ppa:deadsnakes/ppa \  
&& apt-get remove -y software-properties-common \  
&& apt autoremove -y \  
&& apt-get update \  
&& apt-get install -y python3.6 python3.6-dev \  
&& curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \  
&& python3.6 /tmp/get-pip.py \  
&& apt-get install -y ruby git gcc g++ build-essential  
  
# Useful symbolic links  
RUN ln -s /usr/bin/python3.6 /usr/bin/python3  
RUN ln -s /usr/bin/python3.6 /usr/bin/python  
  
RUN pip3 install -U pip numpy scipy requests tqdm  
  
# Install PyTorch from its repository  
RUN pip3 install torch==0.3.1  
RUN pip3 install -U torchvision  
  
RUN python3 -c "import torch; print(\"PyTorch: v\", torch.__version__)"  


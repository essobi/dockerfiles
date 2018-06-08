# docker build --no-cache=true -t keras-theano -f docker-keras-theano .  
FROM ubuntu:16.04  
LABEL maintainer="Mario David <mariojmdavid@gmail.com>"  
  
ENV KERAS_BACKEND theano  
  
RUN mkdir -p /tmp/setup && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
git \  
python3-dev \  
python3-pip \  
python3-setuptools \  
software-properties-common \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install -U pip && \  
pip3 install Theano && \  
pip3 install keras  
  
WORKDIR /home  
CMD ["/bin/bash"]  
  


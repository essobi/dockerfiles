FROM ubuntu:16.04  
MAINTAINER Kirill Pavlov <kirill.pavlov@phystech.edu>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
python3.5-minimal \  
python3.5-dev \  
python3-pip \  
# numpy  
liblapack-dev \  
libopenblas-dev \  
libatlas-base-dev \  
# matplotlib  
libxft-dev \  
libfreetype6-dev  
  
RUN pip3 install --upgrade pip  
  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
RUN pip install setuptools==28.6.0  
  
RUN pip install \  
numpy==1.11.2 \  
scipy==0.18.1 \  
matplotlib==1.5.3 \  
pandas==0.19.0 \  
seaborn==0.7.1 \  
xgboost==0.6a2 \  
plotly==1.12.9 \  
sympy==1.0 \  
scikit-learn==0.18 \  
jupyter==1.0.0  
  
RUN pip install \  
Theano==0.8.2 \  
Keras==1.1.0 \  
https://github.com/Lasagne/Lasagne/archive/master.zip  
  
# RUN pip3 install --upgrade
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.6.0-cp34-none-
linux_x86_64.whl  
WORKDIR /notebooks  
  
ENTRYPOINT ["/tini", "--"]  


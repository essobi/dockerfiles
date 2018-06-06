FROM ubuntu:16.04  
MAINTAINER Julian Rachman <jmrachman@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
git \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
python3-tk \  
rsync \  
software-properties-common \  
unzip \  
vim \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
  
RUN pip --no-cache-dir install \  
GitPython \  
Pillow \  
elasticsearch \  
h5py \  
ipykernel \  
jupyter \  
jupyter-cjk-xelatex \  
matplotlib \  
nbconvert \  
numpy \  
pandas \  
requests \  
scipy \  
sklearn \  
zeep \  
&& \  
python3 -m ipykernel.kernelspec  
  
# --- DO NOT EDIT OR DELETE BETWEEN THE LINES --- #  
RUN pip install tensorflow==1.2.1  
# --- ~ DO NOT EDIT OR DELETE BETWEEN THE LINES --- #  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
COPY notebooks /notebooks  
  
COPY run_jupyter.sh /notebooks/config  
  
EXPOSE 6006  
EXPOSE 8888  
WORKDIR "/notebooks"  
  
RUN cd config && chmod +x run_jupyter.sh  


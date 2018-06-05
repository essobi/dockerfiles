# Adapted from
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/Dockerfile  
FROM ubuntu:14.04  
  
LABEL maintainer="Craig Citro <craigcitro@google.com>"  
EXPOSE 5005  
  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
rsync \  
screen \  
software-properties-common \  
unzip \  
vim \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip \--no-cache-dir install \  
xlrd \  
beautifulsoup4 \  
Pillow \  
Flask \  
matplotlib \  
numpy \  
pandas \  
scipy \  
tqdm  
# --- DO NOT EDIT OR DELETE BETWEEN THE LINES --- #  
# These lines will be edited automatically by parameterized_docker_build.sh. #  
# COPY _PIP_FILE_ /  
# RUN pip --no-cache-dir install /_PIP_FILE_  
# RUN rm -f /_PIP_FILE_  
# Setup logging enviroment  
RUN mkdir /logs  
RUN touch /logs/run.log  
  
# Add the entire repository content to container home  
COPY . /  
  
# Run the flask server  
# RUN python main.py --config=/equATR/config/example.cfg  


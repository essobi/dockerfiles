FROM debian:sid-slim  
  
MAINTAINER Loic Gouarin "loic.gouarin@gmail.com"  
# Configure environment  
ENV CONDA_DIR=/opt/conda CONDA_VER=4.3.11  
ENV PATH=$CONDA_DIR/bin:$PATH  
ENV USER=precis  
  
# Install useful packages  
RUN apt-get update && \  
apt-get install -y curl bzip2 build-essential && \  
apt-get clean  
  
# get and install miniconda  
RUN curl
https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-Linux-x86_64.sh -o
mconda.sh  
  
RUN /bin/bash mconda.sh -f -b -p $CONDA_DIR && \  
rm mconda.sh && \  
rm -rf $CONDA_DIR/pkgs/*  
  
COPY environment.yml environment.yml  
RUN conda env create -f environment.yml &&\  
rm -rf $CONDA_DIR/pkgs  
  
ENV PATH=$CONDA_DIR/envs/$USER/bin:$PATH  
ENV CONDA_ENV_PATH=$CONDA_DIR/envs/$USER  
ENV CONDA_DEFAULT_ENV=$USER  
RUN useradd -m $USER  
  
WORKDIR /home/$USER  
USER $USER  


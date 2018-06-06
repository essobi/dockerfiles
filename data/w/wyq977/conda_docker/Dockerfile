FROM ubuntu:16.04  
MAINTAINER Yongqi WANG <yongqi.wang.cn@gmail.com>  
  
# This is built on the https://hub.docker.com/r/continuumio/miniconda3/  
# I only build this for my own convenience  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
  
WORKDIR /snakemake  
  
RUN git clone https://github.com/wyq977/snakemake_chipseq.git /snakemake/git  
  
# Add the conda channels  
RUN conda config --add channels r && \  
conda config --add channels defaults && \  
conda config --add channels conda-forge && \  
conda config --add channels bioconda  
  
# install dependencies into isolated environment  
# add sambamba  
RUN conda env create --name py35 --file /snakemake/git/envs/py35.yaml  
  
RUN conda env create --name py27 --file /snakemake/git/envs/py27.yaml  
  
# Clean up  
RUN rm -rf /snakemake/git/*  


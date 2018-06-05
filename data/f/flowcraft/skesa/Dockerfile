# DOCKERFILE for skesa  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bash \  
bzip2 \  
git \  
python3 \  
wget  
  
WORKDIR /NGStools  
  
# INSTALL MINICONDA  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh  
RUN ./Miniconda3-latest-Linux-x86_64.sh -b -p /NGStools/miniconda  
ENV PATH="/NGStools/miniconda/bin:$PATH"  
# Configure channels for bioconda  
RUN conda update -y -n base conda && conda config --add channels conda-forge
&& conda config --add channels defaults && conda config --add channels
bioconda  
  
RUN conda install -y skesa  
  
WORKDIR /data/  


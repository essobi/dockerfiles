FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
  
WORKDIR /NGStools/  
  
# Temporary dependencies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget bzip2  
  
# Dependencies  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
&& \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /NGStools/miniconda3 && \  
rm Miniconda3-latest-Linux-x86_64.sh  
  
ENV PATH="/NGStools/miniconda3/bin:${PATH}"  
# sistr_cmd  
RUN conda update -y -n base conda && \  
conda config --add channels conda-forge && \  
conda config --add channels defaults && \  
conda config --add channels bioconda && \  
conda install -y sistr_cmd  
  
# Clean  
RUN apt-get remove -y wget bzip2 && \  
apt-get autoclean -y  
  
WORKDIR /data/  


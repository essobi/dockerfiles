# DOCKERFILE for ipyrad  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bzip2 \  
python-pip \  
gzip \  
wget  
  
WORKDIR /NGStools  
  
# INSTALL MINICONDA  
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh  
RUN chmod +x Miniconda2-latest-Linux-x86_64.sh  
RUN ./Miniconda2-latest-Linux-x86_64.sh -b -p /NGStools/miniconda  
ENV PATH="/NGStools/miniconda/bin:$PATH"  
# Configure channels for bioconda  
RUN conda config --add channels defaults && conda config --add channels conda-
forge && conda config --add channels bioconda  
  
# INSTALL abricate  
RUN conda update conda  
RUN conda install jupyter  
RUN conda install -c ipyrad ipyrad  
RUN pip install jupyter  
  


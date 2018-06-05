# DOCKERFILE for prokka https://github.com/tseemann/abricate  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bzip2 \  
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
RUN conda install prokka  
RUN conda install barrnap  
RUN prokka --setupdb  
  


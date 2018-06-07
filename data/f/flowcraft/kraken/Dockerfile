FROM ubuntu:16.04  
MAINTAINER I Mendes <cimendes@medicina.ulisboa.pt>  
  
WORKDIR /NGStools/  
  
# INSTALL DEPENDENCIES  
RUN apt-get update && apt-get -y install \  
bzip2 \  
gzip \  
python \  
python3 \  
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
  
# INSTALL kraken  
RUN conda install -c bioconda kraken  
  
# minikraken DB 4GB RefSeq Oct. 18, 2017  
RUN mkdir /kraken_db/ && cd /kraken_db/ && wget
https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz && tar xf
minikraken_20171019_4GB.tgz && rm minikraken_20171019_4GB.tgz  
  
ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"
KRAKEN_DB_PATH="/kraken_db:${KRAKEN_DB_PATH}"  
WORKDIR /data/


# DOCKERFILE for abricate https://github.com/tseemann/abricate  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bzip2 \  
gzip \  
wget \  
git  
# git needs to be present to allow DB update  
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
  
# ADD Virulence_finder database  
RUN git clone https://bitbucket.org/genomicepidemiology/virulencefinder_db.git
&& cd virulencefinder_db && cat *.fsa >> sequences  
  
# INSTALL abricate  
RUN conda install -y abricate  
#RUN mkdir -p /NGStools/miniconda3/db/Virulence_finder && cp
virulencefinder_db/sequences /NGStools/miniconda3/db/Virulence_finder  
RUN abricate --check && abricate --setupdb  
RUN cd /NGStools/miniconda/db && mkdir virulencefinder && cp
/NGStools/virulencefinder_db/sequences virulencefinder/ && abricate --setupdb  
  
WORKDIR /data/  


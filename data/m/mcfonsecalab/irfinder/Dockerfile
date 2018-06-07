FROM mcfonsecalab/python36_bio  
  
MAINTAINER Rui Luis <rluis@medicina.ulisboa.pt>  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
#RUN conda update -n base conda  
LABEL irfinder="v1.2.3"  
LABEL star="v2.6.0b"  
LABEL bedtools="v2.27.1"  
RUN conda install -c bioconda irfinder star bedtools  
  
RUN apt-get autoclean -y  


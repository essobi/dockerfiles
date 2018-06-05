# Set the base image to debian based miniconda3  
FROM conda/miniconda3  
  
# File Author / Maintainer  
MAINTAINER Matthias Becker  
  
RUN conda config \--add channels r  
RUN conda config \--add channels defaults  
RUN conda config \--add channels conda-forge  
RUN conda config \--add channels bioconda  
  
RUN conda install -y hisat2=2.1.0  
RUN conda install -y zstd  
RUN conda install -y pigz  
RUN conda install -y fastp=0.13.1  


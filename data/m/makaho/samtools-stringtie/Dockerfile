# Set the base image to debian based miniconda3  
FROM conda/miniconda3  
  
# File Author / Maintainer  
MAINTAINER Matthias Becker  
  
RUN conda config \--add channels r  
RUN conda config \--add channels defaults  
RUN conda config \--add channels conda-forge  
RUN conda config \--add channels bioconda  
  
RUN conda install -y samtools=1.8  
RUN conda install -y zstd  
RUN conda install -y stringtie=1.3.4  


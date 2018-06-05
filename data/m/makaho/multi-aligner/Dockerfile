# Set the base image to debian based miniconda3  
FROM conda/miniconda3  
  
# File Author / Maintainer  
MAINTAINER Matthias Becker  
  
RUN conda config \--add channels r  
RUN conda config \--add channels defaults  
RUN conda config \--add channels conda-forge  
RUN conda config \--add channels bioconda  
  
RUN conda install -y bowtie=1.2.2  
RUN conda install -y hisat2=2.1.0  
RUN conda install -y star=2.5.4a  
RUN conda install -y kallisto=0.43.1  
RUN conda install -y parallel-fastq-dump=0.6.2


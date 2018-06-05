FROM biocontainers/biocontainers:latest  
  
LABEL base.image="biocontainers:latest"  
LABEL description="Calculate coverage based on a provided BED file"  
LABEL tags="Genomics"  
  
MAINTAINER Wen-Wei Liang <liang.w@wustl.edu>  
  
USER root  
  
RUN conda install bedtools samtools=1.3.1 mosdepth bcftools  
  
WORKDIR /data/  
  


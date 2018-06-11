FROM biocontainers/biocontainers:latest  
  
LABEL base.image="biocontainers:latest"  
LABEL description="GermlineWrapper: Call germline variants from WXS/WGS BAMs"  
LABEL tags="Genomics"  
  
MAINTAINER Wen-Wei Liang <liang.w@wustl.edu>  
  
USER root  
  
RUN conda install git pindel varscan samtools  
WORKDIR /home/biodocker  
RUN git clone https://github.com/ding-lab/germlinewrapper.git  
  


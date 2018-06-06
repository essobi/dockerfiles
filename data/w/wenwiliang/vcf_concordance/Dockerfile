FROM biocontainers/biocontainers:latest  
  
LABEL base.image="biocontainers:latest"  
LABEL description="Comparison of different VCF files"  
LABEL tags="Genomics"  
  
MAINTAINER Wen-Wei Liang <wenwiliang@gmail.com>  
  
USER root  
  
RUN apt-get update  
RUN apt-get install tabix  
RUN pip install --upgrade pip  
RUN pip install pyvcf pandas  


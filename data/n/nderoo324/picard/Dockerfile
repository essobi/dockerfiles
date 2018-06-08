# Base Image  
FROM biocontainers/biocontainers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="2"  
LABEL software="Picard"  
LABEL software.version="2.0.1"  
LABEL description="A set of Java command line tools for manipulating high-
throughput sequencing (HTS) data and formats."  
LABEL website="https://github.com/picard/picard"  
LABEL documentation="https://github.com/picard/picard"  
LABEL license="https://github.com/picard/picard"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Andrew Wong <nderoo.wong@gmail.com>  
  
RUN conda install picard=2.0.1  
  
WORKDIR /data/  
USER root  
  
ENTRYPOINT ["picard"]  


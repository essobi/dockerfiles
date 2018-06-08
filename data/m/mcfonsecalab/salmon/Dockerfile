  
FROM biocontainers/biocontainers:latest  
  
MAINTAINER Rui Luis <ruisergioluis@gmail.com>  
  
ENV SALMON_VERSION 0.8.1  
RUN conda install salmon=${SALMON_VERSION}  
  
WORKDIR /data/  
  
CMD ["salmon"]  
  


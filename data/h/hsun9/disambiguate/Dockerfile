FROM biocontainers/biocontainers:latest  
  
LABEL software="Disambiguate"  
LABEL software.version="2016.11.10"  
  
RUN conda install -c bioconda bamtools=2.4.0  
RUN conda install -c bioconda ngs-disambiguate=2016.11.10  
  
WORKDIR /data  
  
CMD ["ngs-disambiguate"]  


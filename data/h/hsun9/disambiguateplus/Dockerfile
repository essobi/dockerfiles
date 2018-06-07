FROM biocontainers/biocontainers:latest  
  
LABEL software="BWA"  
LABEL software="Samtools"  
LABEL software="picard"  
LABEL software="Disambiguate"  
LABEL software="STAR"  
  
RUN conda install -c bioconda bwa=0.7.15  
RUN conda install -c bioconda samtools=1.5  
RUN conda install -c bioconda picard=2.17.11  
RUN conda install -c bioconda bamtools=2.4.0  
RUN conda install -c bioconda ngs-disambiguate=2016.11.10  
RUN conda install -c bioconda star=2.5.4a  
  
WORKDIR /data  
  
CMD ["bwa"]  
CMD ["samtools"]  
CMD ["picard"]  
CMD ["ngs_disambiguate"]  
CMD ["STAR"]  


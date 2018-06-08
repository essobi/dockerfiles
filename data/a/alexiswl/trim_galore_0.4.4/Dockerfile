# Base Image  
FROM alexiswl/containers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="Trim Galore"  
LABEL software.version="0.4.4"  
LABEL description="A wrapper tool around Cutadapt and FastQC to consistently
apply quality and adapter trimming to FastQ files"  
LABEL
website="https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/"  
LABEL
documentation="https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/"  
LABEL
license="https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Alexis Lucattini <alexis.lucattini@agrf.org.au>  
  
RUN conda install -c conda-forge perl=5.22.0  
RUN conda install -c bioconda trim-galore=0.4.4  
  
WORKDIR /data/  
  
ENTRYPOINT ["trim_galore"]  


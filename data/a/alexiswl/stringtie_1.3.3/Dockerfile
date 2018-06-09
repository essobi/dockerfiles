# Base Image  
FROM alexiswl/containers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="Stringtie"  
LABEL software.version="1.3.3"  
LABEL description="StringTie is a fast and highly efficient assembler of RNA-
Seq alignments into potential transcripts."  
LABEL website="https://ccb.jhu.edu/software/stringtie/"  
LABEL documentation="https://ccb.jhu.edu/software/stringtie/"  
LABEL license="https://ccb.jhu.edu/software/stringtie/#contact"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Alexis Lucattini <alexis.lucattini@agrf.org.au>  
  
RUN conda install -c bioconda stringtie=1.3.3  
  
WORKDIR /data/  
  
ENTRYPOINT ["stringtie"]  


# Base Image  
FROM alexiswl/containers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="Sortmerna"  
LABEL software.version="2.0"  
LABEL description="SortMeRNA is a program tool for filtering, mapping and OTU-
picking NGS reads in metatranscriptomic and metagenomic data"  
LABEL website="http://bioinfo.lifl.fr/RNA/sortmerna/"  
LABEL documentation="http://bioinfo.lifl.fr/RNA/sortmerna/code/SortMeRNA-user-
manual-v2.1.pdf"  
LABEL license="http://bioinfo.lifl.fr/RNA/sortmerna/"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Alexis Lucattini <alexis.lucattini@agrf.org.au>  
  
RUN conda install -c biocore sortmerna=2.0  
  
WORKDIR /data/  
  
ENTRYPOINT ["sortmerna"]  


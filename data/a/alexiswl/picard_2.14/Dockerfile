# Base Image  
FROM alexiswl/containers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="picard"  
LABEL software.version="2.14"  
LABEL description="Picard is a set of command line tools for manipulating
high-throughput sequencing (HTS) data"  
LABEL website="http://broadinstitute.github.io/picard/"  
LABEL documentation="http://broadinstitute.github.io/picard/"  
LABEL license="GPLv3"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Alexis Lucattini <alexis.lucattini@agrf.org.au>  
  
RUN conda install -c bioconda picard=2.14  
  
WORKDIR /data/  
  
ENTRYPOINT ["picard"]  


FROM biocontainers/biocontainers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="2"  
LABEL software="bedtools"  
LABEL software.version="2.26.0"  
LABEL description="a powerful toolset for genome arithmetic"  
LABEL website="http://bedtools.readthedocs.io/en/latest/"  
LABEL documentation="http://quinlanlab.org/tutorials/bedtools/bedtools.html"  
LABEL license="https://github.com/arq5x/bedtools2/blob/master/LICENSE"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Andrew Wong <nderoo.wong@gmail.com>  
  
USER root  
  
RUN conda install bedtools=2.26.0  
  
CMD ["bedtools"]  
  


# Base Image  
FROM alexiswl/containers:latest  
  
# Metadata  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="FeatureCounts"  
LABEL software.version="1.5.3"  
LABEL description="a software program developed for counting reads to genomic
features such as genes, exons, promoters and genomic bins"  
LABEL website="bioinf.wehi.edu.au/featureCounts/"  
LABEL documentation="http://subread.sourceforge.net/"  
LABEL license="GPLv3"  
LABEL tags="Genomics"  
  
# Maintainer  
MAINTAINER Alexis Lucattini <alexis.lucattini@agrf.org.au>  
  
RUN conda install -c bioconda subread=1.5.3  
  
WORKDIR /data/  
  
ENTRYPOINT ["featureCounts"]  


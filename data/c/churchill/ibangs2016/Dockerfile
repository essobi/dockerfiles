  
## Based on rocker / hadleyverse maintained by Carl Boettiger and Dirk
Eddelbuettel  
FROM rocker/hadleyverse  
  
MAINTAINER "Daniel Gatti" dan.gatti@jax.org  
  
# install svd package  
RUN install2.r --error svd  
  
# DOQTL and dependencies.  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite(c("AnnotationHub", "DOQTL", "DESeq2", "ggplot2", "dplyr",
"VariantAnnotation"), ask=FALSE)'  
RUN Rscript -e 'install.packages(pkgs = "devtools", dependencies = TRUE)'  
RUN Rscript -e 'library(devtools); install_github(repo = "dmgatti/DOQTL")'  


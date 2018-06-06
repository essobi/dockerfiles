## Start with the hadleyverse image from Rocker, then add population  
## genetics images on top.  
  
FROM rocker/tidyverse:latest  
MAINTAINER Hilmar Lapp hilmar.lapp@duke.edu  
  
# Prevent error messages from debconf about non-interactive frontend  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
## Some of the R packages depend on package gsl, which requires gsl-dev  
## to be installed in order to succeed  
RUN apt-get update \  
&& apt-get install -y libgsl0-dev  
  
## The nloptr package is needed by lme4, and it itself needs to download the  
## NLopt code from http://ab-initio.mit.edu/wiki/index.php/NLopt, which is  
## unstable. Hence we put this upfront, so that we fail fast on this step,  
## which makes it easier to redo.  
RUN install2.r --error \  
nloptr \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
## Bioconductor dependencies of packages we install from CRAN (specifically
pegas)  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite("Biostrings");'  
## Install population genetics packages from CRAN  
RUN rm -rf /tmp/*.rds \  
&& install2.r --error \  
apex \  
ape \  
adegenet \  
adespatial \  
pegas \  
coalescentMCMC \  
mmod \  
poppr \  
strataG \  
rmetasim \  
genetics \  
hierfstat \  
lme4 \  
MuMIn \  
multcomp \  
raster \  
viridis \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
## Bioconductor packages (they may be dependencies)  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite("qvalue");'  
## Install population genetics packages from Github  
## (hierfstat included here temporarily until new release is on CRAN)  
RUN installGithub.r \  
whitlock/OutFLANK \  
bcm-uga/pcadapt \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
## Install other useful packages from CRAN  
RUN install2.r --error \  
knitcitations \  
phangorn \  
phylobase \  
phytools \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  


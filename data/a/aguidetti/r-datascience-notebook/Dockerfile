FROM jupyter/minimal-notebook  
  
MAINTAINER Andrew Guidetti <andrew_Guidetti@hms.harvard.edu>  
  
USER root  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
fonts-dejavu \  
gfortran \  
gcc && apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
# R packages  
# Pin r-base to a specific build number for https://github.com/jupyter/docker-
stacks/issues/210#issuecomment-246081809  
RUN conda config --add channels r && \  
conda install --quiet --yes \  
'rpy2=2.8*' \  
'gcc' \  
'r-base=3.3.1 1' \  
'r-irkernel=0.6*' \  
'r-irdisplay=0.3' \  
'r-plyr=1.8*' \  
'r-devtools=1.11*' \  
'r-dplyr=0.4*' \  
'r-ggplot2=2.1*' \  
'r-tidyr=0.5*' \  
'r-shiny=0.13*' \  
'r-rmarkdown=0.9*' \  
'r-forecast=7.1*' \  
'r-stringr=1.0*' \  
'r-rsqlite=1.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-crayon=1.3*' \  
'r-randomforest=4.6*' && conda clean -tipsy  
  
#install bioconductor packages for R  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e
'biocLite("oligo")'  
  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e
'biocLite("org.Hs.eg.db")'  
  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e
'biocLite("VariantAnnotation")'  
  
RUN Rscript -e 'source("http://bioconductor.org/workflows.R")' -e
'workflowInstall("variants")'  
  
RUN Rscript -e 'library(devtools)' -e 'install_github("Gastrograph/RS3")'  


FROM jupyter/minimal-notebook  
  
MAINTAINER Evandro Dutra <evandro.eld@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -yq \  
fonts-dejavu \  
gfortran \  
gcc && apt-get clean && cd ~ \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
RUN conda install --quiet --yes \  
'r-base=3.3.2' \  
'r-irkernel=0.7*' \  
'r-plyr=1.8*' \  
'r-devtools=1.12*' \  
'r-tidyverse=1.0*' \  
'r-shiny=0.14*' \  
'r-rmarkdown=1.2*' \  
'r-forecast=7.3*' \  
'r-rsqlite=1.1*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-crayon=1.3*' \  
'r-randomforest=4.6*' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  


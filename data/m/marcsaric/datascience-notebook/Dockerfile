# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM marcsaric/scipy-notebook  
  
LABEL maintainer="Marc Saric <marc.saric@gmx.de>"  
# Set when building on Travis so that certain long-running build steps can  
# be skipped to shorten build time.  
ARG TEST_ONLY_BUILD  
  
USER root  
  
# R pre-requisites # FIXME: Those are already in the minimal notebook?  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
fonts-dejavu \  
tzdata \  
libmariadb-client-lgpl-dev \  
gfortran \  
gcc && apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Fix a bug in some R-packages, which want /bin/gtar instead of /bin/tar  
RUN ln -s /bin/tar /bin/gtar  
  
USER $NB_UID  
  
# R packages including IRKernel which gets installed globally.  
# Adjusted versions to latest major and minor digits  
RUN conda config --system --append channels r && \  
conda install --quiet --yes \  
'gcc_linux-64' \  
'gxx_linux-64' \  
'gfortran_linux-64' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
conda install --quiet --yes \  
'rpy2=2.9*' \  
'rstudio=1.1*' \  
'r-base=3.4.2' \  
'r-irkernel=0.8*' \  
'r-plyr=1.8*' \  
'r-devtools=1.13*' \  
'r-tidyverse=1.1*' \  
'r-shiny=1.0*' \  
'r-rmarkdown=1.8*' \  
'r-forecast=8.2*' \  
'r-rsqlite=2.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-crayon=1.3*' \  
'r-randomforest=4.6*' \  
'r-htmltools=0.3*' \  
'r-sparklyr=0.7*' \  
'r-htmlwidgets=1.0*' \  
'r-hexbin=1.27*' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
# Add TCGAbiolinks from Bioconductor  
RUN R -e
'source("https://bioconductor.org/biocLite.R");biocLite("TCGAbiolinks")'  


# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM marcsaric/scipy-notebook  
  
LABEL maintainer="Marc Saric <marc.saric@gmx.de>"  
  
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
  
USER $NB_USER  
  
# Add Biopython and other bioinformatics tools from Conda  
RUN conda install --quiet --yes \  
-c anaconda biopython && \  
conda install -c bioconda pysam && \  
conda install -c bioconda pysamstats  
  
RUN conda install -c conda-forge jupyter_contrib_nbextensions  
  
RUN conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  


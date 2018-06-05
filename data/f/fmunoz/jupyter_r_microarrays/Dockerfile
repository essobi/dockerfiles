# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/minimal-notebook  
  
MAINTAINER Jupyter Project <jupyter@googlegroups.com>  
  
USER root  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libpangoft2-1.0-0 \  
libxt-dev \  
xvfb \  
xauth \  
xfonts-base \  
libglib2.0-0 \  
libglib2.0-bin \  
libpango-1.0-0 \  
libcurl4-openssl-dev \  
libxml2-dev \  
libglib2.0-dev \  
libgdk-pixbuf2.0-dev \  
libatk1.0-dev \  
libssl-dev \  
libpangocairo-1.0-0\  
libcairo2 \  
libcairo2-dev \  
libgtk2.0-dev \  
libpango1.0-dev \  
fonts-dejavu \  
gfortran \  
libssh2-1-dev \  
libssl-dev \  
r-cran-xml \  
libnlopt-dev \  
xml-core \  
gcc && apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
USER $NB_USER  
  
# R packages  
# Pin r-base to a specific build number for https://github.com/jupyter/docker-
stacks/issues/210#issuecomment-246081809  
RUN conda config --add channels r && \  
conda install --quiet --yes \  
'conda-build' \  
'gcc' \  
'r-base=3.3.1 1' \  
'r-irkernel=0.7*' \  
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
'r-randomforest=4.6*' && conda update conda && conda clean -tipsy  
  
RUN Rscript -e "install.packages(c('gridSVG','cdfname','xml', 'gcc',
'irkernel', 'plyr', 'devtools', 'dplyr', 'gplots', 'ggplot2', 'tidyr',
'shiny', 'rmarkdown', 'forecast', 'stringr', 'rsqlite','reshape2',
'nycflights13', 'caret', 'rcurl', 'crayon', 'randomforest', 'Cairo'),
repos='https://cloud.r-project.org')"  
  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R'); biocLite()"  
  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R'); biocLite(c( \  
'annotate', \  
'limma', \  
'affy', \  
'GEOquery', \  
'SVGAnnotation', \  
'affxparser' , \  
'simpleaffy', \  
'hgu133a.db', \  
'hgu133a2.db', \  
'hgu133plus2.db', \  
'hugene10sttranscriptcluster.db', \  
'oligo', \  
'frma', \  
'hgu133afrmavecs', \  
'hgu133plus2frmavecs', \  
'hgu133plus2cdf', \  
'hgu133acdf', \  
'hugene10stv1cdf', \  
'arrayQualityMetrics', \  
'genefilter', 'pathifier' ));"  
  
  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite(c('GEOquery'));"  


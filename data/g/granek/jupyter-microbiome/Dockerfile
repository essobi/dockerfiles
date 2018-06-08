# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
  
# Derived from:  
# wget https://raw.githubusercontent.com/jupyter/docker-
stacks/master/r-notebook/Dockerfile  
# wget https://raw.githubusercontent.com/jupyter/docker-
stacks/master/datascience-notebook/Dockerfile  
# wget https://raw.githubusercontent.com/jupyter/docker-stacks/master/scipy-
notebook/Dockerfile  
# See https://github.com/jupyter/docker-stacks  
  
FROM jupyter/r-notebook  
  
MAINTAINER Josh Granek <josh@duke.edu>  
  
USER root  
  
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
# Install Less  
##~~~~~~~~~~~~  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
less \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
  
##---------------------------------------------------------------------------  
# Install Python 2 and Bash Kernel  
##--------------------------------  
USER jovyan  
  
# Install Python 2 packages  
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \  
'ipython=4.1*' \  
'ipywidgets=4.1*' \  
'matplotlib=1.5*' \  
&& conda clean -tipsy  
  
# Install Bash Kernel  
RUN pip install --user --no-cache-dir bash_kernel && \  
python -m bash_kernel.install  
  
USER root  
  
# Install Python 2 kernel spec globally to avoid permission problems when
NB_UID  
# switching at runtime.  
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install  
##---------------------------------------------------------------------------  
  
##===========================================================================  
# Install qiime  
#=================  
# Is pip install sufficient, or do we need to use apt-get to get dependencies?  
# pypi has qiime version 1.9.1, while debian stable (jessie) only has 1.8.0  
  
#=================  
# pip approach  
#=================  
USER jovyan  
RUN $CONDA_DIR/envs/python2/bin/pip install qiime  
ENV PATH=${PATH}:$CONDA_DIR/envs/python2/bin  
  
#=================  
# apt-get approach  
#=================  
# USER root  
# RUN apt-get update && \  
# apt-get install -y --no-install-recommends \  
# qiime \  
# && apt-get clean && \  
# rm -rf /var/lib/apt/lists/*  
##===========================================================================  
  
##===========================================================================  
# Install dada and its dependencies  
#=================  
USER jovyan  
#setup R configs  
RUN conda install gcc \  
&& conda clean -tipsy  
# RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'https://cran.revolutionanalytics.com/'; options(repos =
r);options(download.file.method = 'wget')" > ~/.Rprofile  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.revolutionanalytics.com/'; options(repos = r)" > ~/.Rprofile  
RUN Rscript -e
"source('http://bioconductor.org/biocLite.R');biocLite(suppressUpdates =
FALSE);biocLite('ShortRead', suppressUpdates = FALSE);biocLite('phyloseq',
suppressUpdates = FALSE)"  
# RUN Rscript -e
"library('devtools');devtools::install_github('benjjneb/dada2')"  
RUN Rscript -e "library('devtools');library(RCurl);library(httr);set_config(
config( ssl_verifypeer = 0L ) );devtools::install_github('benjjneb/dada2')"  
  
  
USER jovyan  


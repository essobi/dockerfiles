# Copyright (c) Mihai Paraschiv.
# Distributed under the terms of the Modified BSD License.

FROM jupyter/scipy-notebook:1d374670daaa
MAINTAINER Mihai Paraschiv <mihai.paraschiv@gmail.com>


# Install required OS packages ################################################

USER root

# libraries needed for R and rpy2
# x11 is needed for plotting in r
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    gcc \
    libreadline-gplv2-dev \
    x11vnc \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER


# Install Python packages in Python 3 environment #############################
# Update packages available in Anaconda
RUN conda install -n root --quiet --yes \
'seaborn' \
    && conda clean -tipsy

# Install other Python packages
RUN pip3 install \
'lifelines==0.9.*' \
'lifetimes==0.2.*' \
'matplotlib_venn==0.11.*' \
'git+git://github.com/paulgb/sklearn-pandas.git@7a3c997a00d23135cfcfe6320c4886cdbccf6ee8'
# Install R ###################################################################
# Install R in Python 3 environment
RUN conda config --add channels r && \
    conda install --quiet --yes \
'r-base=3.3*' \
'rpy2=2.8*' \
'r-irkernel=0.6*' \
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
'r-caret=6.0*' \
'r-rcurl=1.95*' \
'r-randomforest=4.6*' \
'r-lubridate=1.5*' \
    && conda clean -tipsy

# Install additional R packages
RUN R --vanilla -e "\
    install.packages(c('ROCR', 'BTYD'), \
    repos='http://cran.us.r-project.org', \
    lib='${CONDA_DIR}/lib/R/library')"

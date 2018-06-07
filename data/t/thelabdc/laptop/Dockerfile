FROM jupyter/scipy-notebook  
  
USER root  
  
RUN apt-get update && apt-get install -y tofrodos  
COPY vimrc /home/jovyan/.vimrc  
COPY harlequin.vim /home/jovyan/.vim/colors/harlequin.vim  
RUN chown -R jovyan:users /home/jovyan/.vim  
  
# standard vim setup  
USER jovyan  
RUN fromdos -d /home/jovyan/.vimrc && \  
fromdos -d /home/jovyan/.vim/colors/harlequin.vim  
  
# R packages including IRKernel which gets installed globally.  
RUN conda install --quiet --yes --channel conda-forge \  
'rpy2=2.8*' \  
'r-base=3.4.1*' \  
'r-irkernel=0.7*' \  
'r-plyr=1.8*' \  
'r-devtools=1.13.2' \  
'r-tidyverse=1.1.1' \  
'r-shiny=1.0.3' \  
'r-rmarkdown=1.6' \  
'r-forecast=8.0' \  
'r-rsqlite=1.1*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-crayon=1.3*' \  
'r-randomforest=4.6*' && conda clean -tipsy  
  
# Install geos things and dnsutils  
USER root  
RUN apt-get update \  
&& apt-get install -y libgeos-dev libgdal-dev libproj-dev dnsutils  
USER jovyan  
RUN conda install -y geopandas -c conda-forge  
  
# Install MS ODBC Drivers  
USER root  
ENV ACCEPT_EULA=Y  
RUN apt-get update && apt-get install -y apt-transport-https && \  
sh -c 'curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -'
&& \  
sh -c 'curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list' && \  
apt-get update && \  
apt-get install -y msodbcsql mssql-tools unixodbc-dev && \  
rm -rf /var/lib/apt/lists/*  
USER jovyan  
RUN conda install pyodbc -c conda-forge  
  
# Install tox  
RUN conda install -y tox pystan lxml  
  
# Install some R things  
RUN Rscript -e 'options(repos="https://cran.rstudio.com");
install.packages(c("ggplot2", "rgeos", "maptools", "pacman", "mosaic",
"weights", "knitr", "kableExtra", "foreign", "fastLink", "wru", "lubridate",
"stringr", "reshape2", "texreg", "RItools", "foreign", "readstata13", "Hmisc",
"dplyr", "scales", "rgdal", "ggmap", "raster", "gridExtra", "sp", "spdep"))'  


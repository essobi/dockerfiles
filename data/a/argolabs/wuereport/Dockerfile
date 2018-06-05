# get the base image, this one has R, RStudio and pandoc  
FROM rocker/verse:latest  
  
LABEL maintainer="ctull17@gmail.com"  
  
COPY . /wueReport  
  
# go into the repo directory  
RUN apt-get update \  
  
&& . /etc/environment \  
# install package deps from specific commits for reproducibility  
&& R -e "devtools::install_github('ropensci/plotly',
ref='2077abf09064b9d4896c7b21ec6d3a94105c9119', vignettes=FALSE)" \  
  
&& R -e "devtools::install_github('tidyverse/ggplot2',
ref='41f154f5eb89f9939c149645611a5834eb674309', vignettes=FALSE)" \  
  
&& R -e "install.packages('leaflet')" \  
&& R -e "install.packages('ggmap')" \  
&& R -e "install.packages('leaflet.extras')" \  
&& R -e "install.packages('data.table')" \  
&& R -e "install.packages('plyr')" \  
&& R -e "install.packages('DT')" \  
&& R -e "install.packages('dbplyr')" \  
# build this package  
&& R -e "devtools::install('/wueReport', dep=FALSE)" \  


# Driver Script  
# Ted Haley Dec 2017  
# Runs a Docker Container  
#Usage:  
# `cd Path-To-Local-Repo/tree_value`  
# `git clone https://github.com/TedHaley/tree_value.git`  
# `docker pull teddyhaley/tree_value`  
# `docker run --rm -it -v /Path-To-Local-Repo/tree_value:/home/tree_value
teddyhaley/tree_value /bin/bash`  
# `cd home/tree_value/`  
# `make clean`  
# `make all`  
FROM rocker/tidyverse  
  
RUN Rscript -e "install.packages('devtools')"  
  
RUN Rscript -e "install.packages('ezknitr')"  
  
RUN Rscript -e "install.packages('lubridate')"  
  
RUN Rscript -e "install.packages('dplyr')"  
  
RUN Rscript -e "install.packages('readr')"  
  
RUN Rscript -e "install.packages('ggplot2')"  
  
RUN Rscript -e "install.packages('rgdal')"  
  
RUN Rscript -e "install.packages('broom')"  
  
RUN Rscript -e "install.packages('maptools')"  
  
RUN Rscript -e "install.packages('gpclib')"  
  
RUN Rscript -e "install.packages('packrat')"  
  
RUN Rscript -e "install.packages('MASS')"  
  
RUN Rscript -e "install.packages('scales')"  
  
RUN Rscript -e "install.packages('stringr')"  
  
RUN Rscript -e "install.packages('hexbin')"  
  
RUN Rscript -e "install.packages('reshape2')"  
  
RUN Rscript -e "install.packages('ggmap', repos =
'http://cran.us.r-project.org')"  
  


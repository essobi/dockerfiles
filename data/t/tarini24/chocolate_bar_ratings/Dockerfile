# Docker file for Chocolate Bar Ratings project  
# Tarini Bhatnagar, December 2017  
# This script creates the Docker container with the tools needed to execute
the entire project.  
# use rocker/tidyverse as the base image  
FROM rocker/tidyverse  
  
# install ezknitr packages  
RUN Rscript -e "install.packages('ezknitr', repos =
'http://cran.us.r-project.org')"  
  
# install packrat package  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
  
# install colorRamps package  
RUN Rscript -e "install.packages('colorRamps', repos =
'http://cran.us.r-project.org')"  
  
# install countrycode package  
RUN Rscript -e "install.packages('countrycode', repos =
'http://cran.us.r-project.org')"  
  
# install knitr package  
RUN Rscript -e "install.packages('knitr', repos =
'http://cran.us.r-project.org')"  
  
# install maps package  
RUN Rscript -e "install.packages('maps', repos =
'http://cran.us.r-project.org')"  
  
# install RColorBrewer package  
RUN Rscript -e "install.packages('RColorBrewer', repos =
'http://cran.us.r-project.org')"  


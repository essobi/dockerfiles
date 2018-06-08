# Docker file for forecasting traffic to msn.com  
# Avinash Prabhakaran, May, 2018  
# use rocker/tidyverse as the base image and  
FROM rocker/tidyverse  
  
# Installing other dependencies  
RUN Rscript -e "install.packages('optparse', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages(c('feather', 'moments'), repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages(c('forecast', 'tseries', 'imputeTS'), repos =
'http://cran.us.r-project.org')"  


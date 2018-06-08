# Docker file for Milestone_DSCI522  
# Yue Qian, Dec, 2017  
# Use rocker/tidyverse as the base image  
FROM rocker/tidyverse  
  
# Install broom  
RUN Rscript -e "install.packages('broom', repos =
'http://cran.us.r-project.org')"  
  
# Install knitr  
RUN Rscript -e "install.packages('knitr', repos =
'http://cran.us.r-project.org')"  
  
# Install packrat  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  


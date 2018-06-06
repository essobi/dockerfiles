# Docker file for chopstick_analysis  
# Linsey Yao  
# Dec 17, 2017  
# rocker/tidyverse is the base image  
FROM rocker/tidyverse  
  
# ezknitr for generating the report  
RUN Rscript -e "install.packages('ezknitr', repos =
'http://cran.us.r-project.org')"  
  
# Install packrat  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  


# Docker file for poverty-and-education  
# Adapted almost verbatim from Tiffany Timbers, Dec, 2017  
# (see https://github.com/ttimbers/data_analysis_pipeline_eg)  
# use rocker/tidyverse as the base image  
FROM rocker/tidyverse  
  
# need to install utility to download dataset  
RUN apt-get install -y curl  
  
# then install the needed R packages  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('ezknitr', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('readxl', repos =
'http://cran.us.r-project.org')"  


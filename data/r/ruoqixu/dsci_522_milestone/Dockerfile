# Docker file for DSCI_522_Milestone  
# Ruoqi Xu, Dec. 2017  
#  
# Runs a Docker Container  
# This dockerfile is used in the automated build of the docker image  
#  
# usage: docker run -it --rm -v
YOUR_LOCAL_DIRECTORY_OF_CLONED_REPO/:/home/DSCI_522_Milestone
ruoqixu/dsci_522_milestone /bin/bash  
# Using tidyverse Rocker image as a base image  
FROM rocker/tidyverse  
  
# Install ezknitr  
RUN Rscript -e "install.packages('ezknitr', repos =
'http://cran.us.r-project.org')"  
  
# Install packrat  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
  
# install the knitr packages  
RUN Rscript -e "install.packages('knitr', repos =
'http://cran.us.r-project.org')"  
  
# Install ggplot2  
RUN Rscript -e "install.packages('ggplot2', repos =
'http://cran.us.r-project.org')"  
  
# install the svglite packages  
RUN Rscript -e "install.packages('svglite', repos =
'http://cran.us.r-project.org')"  


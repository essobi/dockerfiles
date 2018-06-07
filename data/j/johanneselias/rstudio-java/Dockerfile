# Base image, see https://hub.docker.com/r/rocker/rstudio  
FROM rocker/rstudio:3.4.2  
# Install java and rJava  
RUN apt-get -y update && apt-get install -y \  
default-jdk \  
r-cran-rjava  
  
# Install further R packages  
RUN Rscript -e
"install.packages(c('dplyr','gdata','glmulti','openxlsx','tidyr'), repos =
'http://ftp.gwdg.de/pub/misc/cran')"  
  
# Initialize rocker/rstudio  
CMD ["/init"]  
  


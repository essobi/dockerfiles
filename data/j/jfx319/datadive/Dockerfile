## Start with the most comprehensive rocker stack (may be a bit bloated, if
you don't need all of these packages...)  
FROM rocker/ropensci:latest  
MAINTAINER jfx319 jfx319@virginia.edu  
  
## Install additional dependencies  
RUN install2.r --error \  
-r 'http://cran.rstudio.com' \  
ggmap \  
tidycensus \  
&& R -e "remotes::install_github('tidyverse/ggplot2')" \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  


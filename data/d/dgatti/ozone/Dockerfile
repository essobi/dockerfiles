## Based on rocker / hadleyverse maintained by Carl Boettiger and Dirk
Eddelbuettel  
FROM rocker/hadleyverse  
  
MAINTAINER "Daniel Gatti" dan.gatti@jax.org  
  
# tidyverse and dependencies.  
RUN Rscript -e 'install.packages(pkgs = "tidyverse", dependencies = TRUE)'  
RUN Rscript -e 'install.packages(pkgs = "lubridate", dependencies = TRUE)'  
RUN Rscript -e 'install.packages(pkgs = "stringr", dependencies = TRUE)'  
  


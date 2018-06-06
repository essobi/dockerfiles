FROM jupyter/datascience-notebook  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libpq-dev  
  
RUN R -e 'options(repos=structure(c(CRAN="http://cran.ma.imperial.ac.uk")));
install.packages(c("RPostgreSQL","ggplot2"))'  
  
ADD files /opt/defaults/  
  
USER jovyan


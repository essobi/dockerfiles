FROM rocker/r-base  
MAINTAINER Rodrigo Belo <rodrigobelo@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y \  
git-core \  
libssl-dev \  
libcurl4-gnutls-dev  
  
RUN R -e 'install.packages(c("data.table", "caret", "gbm", "lubridate"))'  
RUN R -e 'install.packages(c("devtools"))'  
RUN R -e 'devtools::install_github("trestletech/plumber")'  
  
EXPOSE 45572  
CMD Rscript /deploy/server.R  
  


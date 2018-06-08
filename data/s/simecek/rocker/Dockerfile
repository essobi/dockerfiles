## Based on rocker/r-base maintained by Carl Boettiger and Dirk Eddelbuettel  
FROM rocker/r-base  
  
MAINTAINER "Petr Simecek" lamparna@gmail.com  
  
# devtools external dependencies  
RUN apt-get -y update && apt-get -y upgrade && \  
apt-get install -y libcurl4-openssl-dev && \  
apt-get install -y libxml2-dev && \  
apt-get install -y libssl-dev  
  
## install the required R packages  
RUN Rscript -e 'install.packages(pkgs = c("qtl", "abind", "curl"),
dependencies = TRUE)'  
RUN Rscript -e 'install.packages(pkgs = "devtools", dependencies = TRUE)'  
RUN Rscript -e 'install.packages(c("yaml", "jsonlite", "data.table",
"RcppEigen"), dependencies = TRUE)'  
RUN Rscript -e 'devtools::install_github(repo = c("rqtl/qtl2geno",
"rqtl/qtl2scan", "rqtl/qtl2plot", "rqtl/qtl2convert"))'  
RUN Rscript -e 'devtools::install_github("simecek/intermediate")'  
RUN Rscript -e 'devtools::install_github("kbroman/lmmlite")'  
  


## Based on rocker/hadleyverse maintained by Carl Boettiger and Dirk
Eddelbuettel  
FROM rocker/hadleyverse  
  
MAINTAINER "Petr Simecek" lamparna@gmail.com  
  
## install the required R packages  
RUN Rscript -e 'install.packages(pkgs = "qtl", dependencies = TRUE)'  
RUN Rscript -e 'install.packages(pkgs = "abind", dependencies = TRUE)'  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite(c("DOQTL"), ask=FALSE)'  
RUN Rscript -e 'devtools::install_github(repo = "dmgatti/DOQTL")'  
RUN Rscript -e 'install.packages(c("yaml", "jsonlite", "data.table",
"RcppEigen"), dependencies = TRUE)'  
RUN Rscript -e 'devtools::install_github(repo = c("rqtl/qtl2geno",
"rqtl/qtl2scan", "rqtl/qtl2plot", "rqtl/qtl2convert"))'  
RUN Rscript -e 'devtools::install_github("simecek/intermediate")'  
RUN Rscript -e 'devtools::install_github("kbroman/lmmlite")'  
  


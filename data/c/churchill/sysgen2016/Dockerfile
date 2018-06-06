## Based on rocker / hadleyverse maintained by Carl Boettiger and Dirk
Eddelbuettel  
FROM rocker/hadleyverse  
  
MAINTAINER "Daniel Gatti" dan.gatti@jax.org  
  
# install svd package  
RUN install2.r --error svd  
  
# DESeq2, DOQTL and dependencies.  
RUN Rscript -e 'install.packages(pkgs = "qtl", dependencies = TRUE)'  
RUN Rscript -e 'install.packages(pkgs = "abind", dependencies = TRUE)'  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite(c("DESeq2","DOQTL"), ask=FALSE)'  
RUN Rscript -e 'install.packages(pkgs = "devtools", dependencies = TRUE)'  
RUN Rscript -e 'devtools::install_github(repo = "dmgatti/DOQTL")'  
RUN Rscript -e 'install.packages(c("yaml", "jsonlite", "data.table",
"RcppEigen"), dependencies = TRUE)'  
RUN Rscript -e 'devtools::install_github(repo = c("rqtl/qtl2geno",
"rqtl/qtl2scan", "rqtl/qtl2plot", "rqtl/qtl2convert"))'  
RUN Rscript -e 'devtools::install_github("simecek/intermediate")'  
RUN Rscript -e 'devtools::install_github("kbroman/lmmlite")'  
  


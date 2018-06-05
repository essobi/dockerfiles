#################################################################  
# Dockerfile  
# Software: R  
# Description: R and necessary packages to use EventPointer  
# Base Image: R-base:3.4.0  
#################################################################  
  
#R image to be the base in order to build our new image  
FROM r-base:3.4.0  
  
#Maintainer and author  
MAINTAINER Magdalena Arnal <marnal@imim.es>  
  
#Install Ubuntu extensions in order to run r  
RUN apt-get update && apt-get install -y \  
r-cran-xml \  
libssl-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
build-essential \  
curl \  
zlib1g-dev \  
libncurses5-dev  
  
ENV PATH=pkg-config:$PATH  
  
#Install packages from CRAN, github, and bioconductor:  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite(pkgs=c("ballgown","aroma.light","DNAcopy"));'  
RUN Rscript -e 'install.packages("devtools")'  
RUN Rscript -e 'devtools::install_github("alyssafrazee/RSkittleBrewer")'  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite("genefilter" );'  
RUN Rscript -e
'install.packages(c("dplyr","R.utils","aroma.affymetrix","data.table",
"gtools", "Rcpp", "nnls"))'  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite(pkgs=c("DESeq2", "tweeDEseq", "EventPointer", "affxparser", "affy",
"limma"))'  


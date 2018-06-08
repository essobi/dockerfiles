FROM rocker/rstudio:latest  
  
MAINTAINER Miles Smith (miles-smith@omrf.org)  
  
RUN \  
apt-get update -qq && \  
apt-get install -y \  
apt-utils \  
apt-transport-https \  
gnupg \  
zlib1g-dev \  
libssh2-1-dev \  
libcurl4-openssl-dev \  
curl \  
libxml2-dev \  
libssl-dev \  
libnlopt-dev \  
software-properties-common \  
lsb-release \  
vim \  
python3 \  
python3-pip \  
python3.5-venv \  
openjdk-8-jdk \  
libgsl-dev \  
libgsl2 \  
libhdf5-dev \  
libmariadbclient-dev  
  
RUN echo "deb http://packages.cloud.google.com/apt gcsfuse-stretch main" | tee
/etc/apt/sources.list.d/gcsfuse.list; \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update ; apt-get install -y apt-utils kmod && apt-get install -y
gcsfuse  
  
## Install packages from CRAN  
RUN Rscript -e
"source('http://bioconductor.org/biocLite.R');biocLite('devtools');biocLite(c('git2r','igraph','satijalab/Seurat','DESeq2','BiocParallel','MAST','tidyverse',
'monocle', 'pheatmap', 'DDRTree', 'pkathail/magic',
'mojaveazure/loomR','gsl','scone','scater','SingleCellExperiment','zinbwave',
'GSEABase','fgsea','dviraran/xCell'))" \  
&& rm -rf /tmp/downloaded_packages/  
  
RUN echo "library(BiocInstaller)" > $HOME/.Rprofile  


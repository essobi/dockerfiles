FROM r-base:3.3.3  
RUN apt-get update  
RUN apt-get install -y libcurl4-gnutls-dev libxml2-dev  
RUN apt-get install -y libssl-dev  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite(pkgs=c("sva","minfi","lumi","wateRmelon","limma","methylumi","Biobase","IRanges","AnnotationDbi","IlluminaHumanMethylation450k.db","FDb.InfiniumMethylation.hg19","ChAMP"))'  
RUN Rscript -e
'install.packages(c("pryr","Hmisc","compareGroups","MASS","sandwich","lmtest","glmnet","VennDiagram","gplots","parallel"))'  


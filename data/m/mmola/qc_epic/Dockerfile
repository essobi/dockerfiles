FROM r-base:3.4.0  
RUN apt-get update  
RUN apt-get install -y libcurl4-gnutls-dev libxml2-dev  
RUN apt-get install -y libssl-dev  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite(c("minfi","ChAMPdata","Illumina450ProbeVariants.db","sva","IlluminaHumanMethylation450kmanifest","limma","RPMM","DNAcopy","preprocessCore","impute","marray","wateRmelon","goseq","plyr","GenomicRanges","RefFreeEWAS","qvalue","isva","doParallel","bumphunter","quadprog","shiny","shinythemes","plotly","RColorBrewer","DMRcate","dendextend","IlluminaHumanMethylationEPICmanifest","FEM","matrixStats","missMethyl","combinat"))'  
RUN Rscript -e 'install.packages(c("Hmisc","MASS","sandwich","lmtest"))'  


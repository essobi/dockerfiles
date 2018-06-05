FROM keyeoh/totoro_bioc  
  
MAINTAINER Gustavo F. Bayon <fernandezgustavo@uniovi.es>  
  
RUN apt-get install -y libcurl4-openssl-dev xorg-dev libglu1-mesa-dev \  
libxml2-dev  
  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R')" \  
-e "biocLite(c(\  
'BSgenome.Hsapiens.UCSC.hg19',\  
'effsize',\  
'FDb.InfiniumMethylation.hg19',\  
'functional',\  
'GenomicRanges',\  
'ggplot2',\  
'gplots',\  
'graph',\  
'gridExtra',\  
'gtools',\  
'IlluminaHumanMethylation450kmanifest',\  
'minfi',\  
'org.Hs.eg.db',\  
'RBGL',\  
'readr',\  
'reshape2',\  
'statmod',\  
'TxDb.Hsapiens.UCSC.hg19.knownGene'\  
), ask = FALSE)"  
  
RUN apt-get install -y libssl-dev && \  
Rscript -e "install.packages('devtools')" \  
-e "devtools::install_github('keyeoh/epilab', ref = 'totoro')"  
#  
# COPY epilab_0.5.2.tar.gz /  
# RUN R CMD INSTALL epilab_0.5.2.tar.gz  
#  
#  
# RUN Rscript -e "source('http://bioconductor.org/biocLite.R')" \  
# -e "biocLite('topGO', ask = FALSE)"  
# RUN curl
http://download.r-forge.r-project.org/src/contrib/Vennerable_3.0.tar.gz\  
# > Vennerable_3.0.tar.gz  
# RUN R CMD INSTALL Vennerable_3.0.tar.gz  
#  
# RUN apt-get install -y openjdk-7-jdk openjdk-7-jre  
# RUN Rscript -e "source('http://bioconductor.org/biocLite.R')" \  
# -e "biocLite('xlsx', ask = FALSE)"  
#  
# WORKDIR /exosomas  
#  
#  
#  


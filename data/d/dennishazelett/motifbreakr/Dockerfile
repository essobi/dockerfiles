FROM bioconductor/release_core  
  
MAINTAINER Dennis Hazelett "dennis.hazelett at csmc.edu"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN apt-get install -y libxml2-dev libcurl4-openssl-dev gsl-bin libgsl-dev git
\  
libopenblas-base libopenblas-dev liblapack3 liblapack-dev  
  
RUN R -e "biocLite(c('GenomicRanges', 'rtracklayer', 'motifbreakR',
'SNPlocs.Hsapiens.dbSNP142.GRCh37', 'BSgenome.Hsapiens.UCSC.hg19',
'stringr'))"  
  
WORKDIR /home/rstudio  
  
RUN git clone https://bitbucket.org/dennishazelett/motifbreakr \  
&& chmod +x motifbreakr/mb.sh \  
&& mv motifbreakr/mb.sh /usr/bin/mb  
  
RUN chown -R rstudio:staff /home/rstudio/motifbreakr  
VOLUME ["/home/rstudio/data"]  
ENTRYPOINT ["mb"]  


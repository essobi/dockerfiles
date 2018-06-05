FROM mbni/shiny-base  
  
MAINTAINER Keqiang Li "lkq@umich.edu"  
# install dependencies of the app  
RUN R -e "install.packages(c('devtools', 'uuid', 'shinyjs', 'shinythemes',
'curl', 'config', 'readr', 'rjson', 'DBI', 'RSQLite', 'future', 'DT', 'pool',
'tidyverse', 'sendmailR', 'stringr'), repos='https://cran.rstudio.com/')" && \  
# Subread library is still needed for merging bam files.  
R -e "source('https://bioconductor.org/biocLite.R'); biocLite(c('Rsubread',
'tximport', 'rtracklayer', 'GenomicFeatures'))" && \  
R -e "devtools::install_github('keqiang/shinyFiles')"  
COPY tools/samtools /root/samtools  
WORKDIR /root/samtools  
RUN ./configure --prefix=/opt/samtools && make && make install  
  
COPY tools/subread /opt/subread  
COPY tools/hisat2 /opt/hisat2  
COPY tools/STAR /opt/STAR  
COPY tools/salmon /opt/salmon  
  
WORKDIR /shiny_apps/sequence_align  
  
COPY / ./  
  
COPY chown_shinyproxy /opt/chown_shinyproxy  
RUN chmod 700 /opt/chown_shinyproxy  
  
RUN echo "docker ALL=(ALL) NOPASSWD: /opt/chown_shinyproxy" >> /etc/sudoers  
  
#USER 1000  
CMD ["R", "-e", "shiny::runApp('/shiny_apps/sequence_align')"]  


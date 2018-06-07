FROM r-base:latest  
  
MAINTAINER Dusan Randjelovic "dusan.randjelovic@sbgenomics.com"  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
nano \  
wget \  
libxml2-dev  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
RUN R -e "install.packages(c('shiny', 'rmarkdown'),
repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages(c('learnr', 'ggplot2'),
repos='http://cran.rstudio.com/')"  
RUN echo 'source("https://bioconductor.org/biocLite.R")' > /opt/packages.R  
RUN echo 'biocLite(c("Biostrings", "GenomicRanges", "SummarizedExperiment",
"DESeq2", "VariantFiltering", "TxDb.Hsapiens.UCSC.hg38.knownGene",
"TxDb.Hsapiens.UCSC.hg19.knownGene", "BSgenome.Hsapiens.UCSC.hg38",
"BSgenome.Hsapiens.1000genomes.hs37d5", "org.Hs.eg.db", "airway",
"RNAseqData.HNRNPC.bam.chr14"))' >> /opt/packages.R  
RUN Rscript /opt/packages.R  
  
RUN apt-get install -y libssl-dev/unstable  
RUN echo 'source("https://bioconductor.org/biocLite.R")' > /opt/dep_packages.R  
RUN echo 'biocLite(c("ensembldb", "biovizBase", "GenomicScores"))' >>
/opt/dep_packages.R  
RUN Rscript /opt/dep_packages.R  
  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
RUN rm /srv/shiny-server/index.html  
RUN rm -rf /srv/shiny-server/sample-apps  
COPY /stats-intro /srv/shiny-server/  
  
EXPOSE 80  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]


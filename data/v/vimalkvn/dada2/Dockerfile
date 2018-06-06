FROM r-base:3.4.0  
MAINTAINER Vimalkumar Velayudhan <vimalkumarvelayudhan@gmail.com>  
  
# Install dependencies using apt and dada2 from bioconductor  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libcurl4-gnutls-dev \  
libxml2-dev && \  
printf "\  
source('https://bioconductor.org/biocLite.R')\n\  
biocLite(c('dada2', 'phyloseq'))\n\  
install.packages('dplyr')\n\  
q()\n" > /tmp/packages.R && \  
Rscript /tmp/packages.R && \  
rm -rf /var/lib/apt/lists/* /tmp/packages.R  
  
# create and set user for container  
RUN useradd -r -s /sbin/nologin dada2  
USER dada2  
  
ENTRYPOINT ["/usr/bin/Rscript"]  
CMD ["--help"]  
  


# Base Image  
FROM r-base:latest  
  
# Metadata  
LABEL base.image="r-base:3.3.2"  
LABEL version="1.1.0"  
LABEL software="ExomeDepth"  
LABEL software.version="1.1.0"  
LABEL description="R package ExomeDepth is used to perform CNV calling on a
library of BAM files"  
LABEL website="https://CRAN.R-project.org/package=ExomeDepth"  
LABEL documentation="https://CRAN.R-project.org/package=ExomeDepth"  
LABEL license="https://CRAN.R-project.org/package=ExomeDepth"  
LABEL tags="Genomics"  
  
# NBN, BARD1, FANCC currently disabled  
# Maintainer  
MAINTAINER Andrew Wong <nderoo.wong@gmail.com>  
  
RUN apt-get -y update && \  
apt-get --yes --force-yes install libcurl4-openssl-dev  
  
# R dependencies  
RUN Rscript -e
"source('https://bioconductor.org/biocLite.R');biocLite('Biostrings')" && \  
Rscript -e "source('https://bioconductor.org/biocLite.R');biocLite('IRanges')"
&& \  
Rscript -e
"source('https://bioconductor.org/biocLite.R');biocLite('Rsamtools')" && \  
Rscript -e
"source('https://bioconductor.org/biocLite.R');biocLite('GenomicRanges')" && \  
Rscript -e
"source('https://bioconductor.org/biocLite.R');biocLite('GenomicAlignments')"
&& \  
Rscript -e "install.packages('optparse')" && \  
Rscript -e "install.packages('ExomeDepth')"  
  
RUN mkdir /data && \  
mkdir /data/rscripts/  
  
COPY . /data/rscripts/  
  
WORKDIR /data/rscripts/  
  
ENTRYPOINT ["Rscript", "/data/rscripts/dockerExomeDepth.r"]  
  
CMD ["-h"]  


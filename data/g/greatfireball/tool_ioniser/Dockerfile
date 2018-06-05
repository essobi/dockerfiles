FROM ubuntu:xenial  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de"  
LABEL description="Dockerfile providing the ioniser quality assessment
software for MinION long reads"  
  
RUN apt update && apt install --yes software-properties-common python-
software-properties && add-apt-repository --yes ppa:marutter/rrutter  
  
RUN apt update && apt install --yes libcurl4-gnutls-dev r-base  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite(ask=FALSE)' && Rscript -e
'source("https://bioconductor.org/biocLite.R"); biocLite(ask=FALSE)' &&
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("IONiseR",
ask=FALSE)'  
  
VOLUME /data  
  


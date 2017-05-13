# This is a comment
FROM ubuntu:14.04
MAINTAINER blong
RUN apt-get update && apt-get install -y r-base r-base-dev 
RUN echo "Hello world"
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e 'biocLite()'
RUN cat /etc/*release

FROM ubuntu:16.04  
MAINTAINER Etienne Thevenot (etienne.thevenot@cea.fr)  
  
ENV TOOL_VERSION=2.2.7  
ENV CONTAINER_VERSION=1.1  
LABEL version="${CONTAINER_VERSION}"  
LABEL tool_version="${TOOL_VERSION}"  
  
# Add keys for latest R version, needed for biosigner, ubuntu's repo is too
old.  
RUN echo "deb http://cran.univ-paris1.fr/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
# Update system  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y --no-install-recommends r-base git make g++ gfortran  
  
# Clone tool repos  
RUN git clone -b v${TOOL_VERSION}
https://github.com/workflow4metabolomics/biosigner /files/biosigner  
  
# Install requirements  
RUN R -e "install.packages(c('batch', 'randomForest'),
lib='/usr/lib/R/library', dependencies = TRUE,
repos='https://cran.rstudio.com')"  
RUN R -e "source('http://bioconductor.org/biocLite.R') ;
biocLite('biosigner')"  
  
# Clean  
RUN apt-get clean  
RUN apt-get autoremove -y  
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# Make tool accessible through PATH  
ENV PATH=$PATH:/files/biosigner  
  
# Make test script accessible through PATH  
ENV PATH=$PATH:/files/biosigner/test  
  
# Define Entry point script  
ENTRYPOINT ["/files/biosigner/biosigner_wrapper.R"]  


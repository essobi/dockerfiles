FROM ubuntu:16.04  
MAINTAINER Etienne Thevenot (etienne.thevenot@cea.fr)  
  
ENV TOOL_VERSION=2.3.10  
ENV CONTAINER_VERSION=1.1  
LABEL version="${CONTAINER_VERSION}"  
LABEL tool_version="${TOOL_VERSION}"  
  
# Setup package repos  
RUN echo "deb http://cran.univ-paris1.fr/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
# Update system  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y --no-install-recommends r-base git make g++  
  
# Clone tool repos  
RUN git clone -b v${TOOL_VERSION}
https://github.com/workflow4metabolomics/multivariate /files/multivariate  
  
# Install requirements  
RUN R -e "install.packages('batch', lib='/usr/lib/R/library', dependencies =
TRUE, repos='http://mirrors.ebi.ac.uk/CRAN')"  
RUN R -e "source('http://bioconductor.org/biocLite.R') ; biocLite('ropls')"  
  
# Clean  
RUN apt-get clean  
RUN apt-get autoremove -y  
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# Make tool accessible through PATH  
ENV PATH=$PATH:/files/multivariate  
  
# Make test script accessible through PATH  
ENV PATH=$PATH:/files/multivariate/test  
  
# Define Entry point script  
ENTRYPOINT ["/files/multivariate/multivariate_wrapper.R"]  


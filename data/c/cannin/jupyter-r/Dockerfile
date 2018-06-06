FROM jupyter/notebook:stable  
  
# The following would be required to enable exporting of ipynbs but creates
too large an image for docker hub  
# TODO: how to enable adjustbox without pulling down 3G of data  
RUN apt-get update && apt-get install -y inkscape # For nbconvert to work with
svg  
# RUN apt-get update && apt-get install -y texlive-latex-base # For creating
pdfs via latex  
# RUN apt-get update && apt-get install -y texlive-latex-extra # required for
adjustbox.sty, probably is an easier way  
# Install basic commands  
RUN apt-get -y install links nano wget git htop  
  
# Install new version of R  
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
  
RUN cat /etc/apt/sources.list  
  
# Install R  
RUN apt-get update  
RUN apt-get install -y r-base  
RUN apt-get install -y libzmq3-dev # https://github.com/IRkernel/IRkernel  
RUN apt-get install -y libcurl4-gnutls-dev #
http://stackoverflow.com/questions/26445815/error-when-installing-devtools-
package-for-r-in-ubuntu  
RUN apt-get install -y libcurl4-openssl-dev #
http://stackoverflow.com/questions/20671814/non-zero-exit-status-r-3-0-1-xml-
and-rcurl  
RUN apt-get install -y libxml2-dev #
http://stackoverflow.com/questions/20671814/non-zero-exit-status-r-3-0-1-xml-
and-rcurl  
RUN apt-get clean  
  
# Install software needed for common R libraries  
# For RCurl  
RUN apt-get -y install libcurl4-openssl-dev  
# For rJava  
RUN apt-get -y install libpcre++-dev  
RUN apt-get -y install openjdk-7-jdk  
# For XML  
RUN apt-get -y install libxml2-dev  
  
##### PYTHON PACKAGES  
# Install additional python packages  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y python3-pip libzmq3  
RUN pip3 install ipython jinja2 pyzmq tornado pyyaml rpy2  
  
RUN apt-get clean  
  
##### R: COMMON PACKAGES  
# To let R find Java  
RUN R CMD javareconf  
  
# Install R packages  
COPY scripts/installRPackages.R /sbin/installRPackages.R  
RUN chmod +x /sbin/installRPackages.R  
RUN /sbin/installRPackages.R  
  
# Install R packages  
RUN R -e "install.packages(c('devtools', 'gplots', 'httr', 'igraph', 'knitr',
'methods', 'plyr', 'RColorBrewer', 'rJava', 'rjson', 'R.methodsS3', 'R.oo',
'sqldf', 'stringr', 'testthat', 'XML', 'DT', 'htmlwidgets'),
repos='http://cran.rstudio.com/')"  
  
# Install Bioconductor  
RUN R -e "source('http://bioconductor.org/biocLite.R'); biocLite(c('Biobase',
'BiocCheck', 'BiocGenerics', 'BiocStyle', 'S4Vectors', 'IRanges',
'AnnotationDbi'))"  
  
##### INSTALL IPYRMD  
RUN cd /; git clone https://github.com/chronitis/ipyrmd.git  
RUN cd /ipyrmd; python3 setup.py install  
  
EXPOSE 8888  
RUN mkdir /workspace  
VOLUME /workspace  
WORKDIR /workspace  
  
# https://github.com/ipython/ipython/issues/7062  
CMD sh -c "ipython notebook --ip=*"  


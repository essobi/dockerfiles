FROM ubuntu:14.04  
MAINTAINER Alexandra Bomane <alexandra.bomane@univ-paris-diderot.fr>  
  
RUN echo "deb http://cran.r-project.org/bin/linux/ubuntu trusty/" >
/etc/apt/sources.list.d/cran.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get update  
  
RUN apt-get install --yes r-base=3.3.0-1trusty0 r-base-core=3.3.0-1trusty0
r-base-dev=3.3.0-1trusty0 r-base-html=3.3.0-1trusty0 r-doc-html=3.3.0-1trusty0
r-recommended=3.3.0-1trusty0 r-cran-boot=1.3-15-1trusty0 r-cran-
class=7.3-14-1trusty0 r-cran-cluster=2.0.3-1trusty0 r-cran-
codetools=0.2-10-1trusty0 r-cran-foreign=0.8.66-1trusty0 r-cran-
kernsmooth=2.23-15-1trusty0 r-cran-lattice=0.20-33-1trusty0 r-cran-
mass=7.3-44-1trusty0 r-cran-matrix=1.2-6-1trusty0 r-cran-mgcv=1.8-7-1trusty0
r-cran-nlme=3.1.128-1trusty0 r-cran-nnet=7.3-12-1trusty0 r-cran-
rpart=4.1-10-1trusty0 r-cran-spatial=7.3-10-1trusty0 r-cran-
survival=2.39-4-1trusty0  
  
RUN apt-get install --yes wget libcurl4-openssl-dev libssl-dev libxml2-dev  
  
RUN echo 'local({r <\- getOption("repos"); r["CRAN"] <\-
"http://cran.r-project.org"; options(repos=r)})' > ~/.Rprofile  
  
RUN wget http://bioconductor.org/biocLite.R  
  
RUN R -e 'source("biocLite.R"); install.packages("abind"); library(abind);
biocLite("GenomicRanges"); biocLite("methods"); biocLite("Rsamtools")'  
  
RUN rm biocLite.R  
  
RUN wget
https://www.bioconductor.org/packages/3.3/bioc/src/contrib/riboSeqR_1.6.0.tar.gz  
  
RUN R CMD INSTALL riboSeqR_1.6.0.tar.gz  
  
RUN apt-get remove --purge --yes wget  
  
RUN apt-get clean  
  
CMD R --no-save  


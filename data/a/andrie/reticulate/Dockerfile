FROM rocker/rstudio:3.3.3  
ENV CRAN_MIRROR https://mran.microsoft.com/snapshot/2017-06-15  
RUN apt-get update --fix-missing \  
&& apt-get install -y \  
ca-certificates \  
libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
libxml2-dev  
  
# install python3, virtualenv and anaconda  
RUN apt-get install -y \  
python3-pip \  
python3-dev \  
&& pip3 install virtualenv  
  
# install anaconda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
# install R development packages and reticulate  
RUN install2.r --repos ${CRAN_MIRROR}\  
Rcpp \  
devtools \  
roxygen2 \  
knitr \  
rmarkdown \  
yaml \  
reticulate \  
ggplot2 \  
dplyr  
  
# Run rocker/rstudio init  
CMD ["/init"]  


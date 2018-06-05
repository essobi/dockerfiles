FROM debian:8.9  
  
ENV PATH /opt/conda/bin:$PATH  
  
WORKDIR /working  
  
RUN echo "deb http://cran.cnr.berkeley.edu/bin/linux/debian jessie-cran3/" >>
/etc/apt/sources.list \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-key 381BA480 \  
&& apt-get update \  
&& apt-get -y \--force-yes install libcurl4-openssl-dev libssl-dev r-base-core
\  
&& apt-get -y \--force-yes install libxml2-dev \  
&& apt-get -y \--force-yes install wget \  
&& wget \--quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh \  
&& /opt/conda/bin/conda install -y nomkl scikit-learn pandas conda-build \  
&& /opt/conda/bin/conda clean \--all \  
&& R -e "install.packages('dplyr',repos='https://rweb.crmda.ku.edu/cran/')" \  
&& R -e "install.packages('readr',repos='https://rweb.crmda.ku.edu/cran/')" \  
&& R -e "install.packages('stringr',repos='https://rweb.crmda.ku.edu/cran/')"
\  
&& R -e "install.packages('mlr',repos='https://rweb.crmda.ku.edu/cran/')" \  
&& R -e "source('https://bioconductor.org/biocLite.R'); biocLite('GEOquery')"  


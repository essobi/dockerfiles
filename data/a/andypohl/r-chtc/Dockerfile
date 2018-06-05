FROM r-base:latest  
  
MAINTAINER Andy Pohl "apohl@morgridge.org"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
libssl-dev \  
libssh2-1-dev \  
libxml2-dev \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN Rscript -e "install.packages(c('igraph', 'miniCRAN', 'devtools',
'packrat'), type='source')" && \  
Rscript -e "source('https://bioconductor.org/biocLite.R')" && \  
curl -o /etc/R/findlibs.R
https://raw.githubusercontent.com/andypohl/DotR/master/findlibs.R  
  
COPY Rprofile.findlibs.site /etc/R/  
COPY install.r /usr/bin/  
ENV R_PROFILE=/etc/R/Rprofile.findlibs.site  
  
CMD ["bash"]  


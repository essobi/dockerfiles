# PhenoMeNal H2020  
# Microservices - IPO  
FROM container-registry.phenomenal-h2020.eu/phnmnl/xcms  
  
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com
)  
  
LABEL software=IPO  
LABEL software.version=1.4.1  
LABEL version=0.8  
LABEL base.image="container-registry.phenomenal-h2020.eu/phnmnl/xcms"  
LABEL description="A Tool for automated Optimization of XCMS Parameters"  
LABEL website="https://github.com/phnmnl/container-ipo"  
LABEL documentation="https://github.com/phnmnl/container-ipo"  
LABEL license="https://github.com/phnmnl/container-ipo/blob/develop/LICENSE"  
LABEL tags="Metabolomics"  
  
# Add IPO scripts and W4M wrapper to path  
COPY scripts/* /usr/local/bin/  
  
# Install dependencies  
######  
# The installation with github "grimbough/Rhdf5lib" can be deleted when R
3.5.0 will be available.  
# Rhdf5lib >= 1.1.4 is required by 'sneumann-mzR-4f83846'  
######  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget \  
ca-certificates \  
make \  
gcc \  
gfortran \  
g++ \  
r-base-dev \  
libblas-dev \  
liblapack-dev \  
libboost-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
libssh2-1-dev \  
libxml2-utils \  
icu-devtools \  
netcdf-bin && \  
echo 'options("repos"="http://cran.rstudio.com")' >> /etc/R/Rprofile.site && \  
R -e 'install.packages("devtools"); library("devtools");
install_github("grimbough/Rhdf5lib"); install_github("sneumann/mzR");
install.packages(c("batch", "rsm"))' && \  
R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("IPO");' && \  
apt-get --purge -y --auto-remove remove make gcc gfortran g++
libcurl4-openssl-dev libssl-dev libssh2-1-dev libboost-dev && \  
apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
/var/lib/{cache,log}/ /tmp/* /var/tmp/*  
  
# Add testing to container  
COPY runTest1.sh /usr/local/bin/runTest1.sh  
  
# Define Entry point script (Warning: may break Galaxy scripts!)  
#ENTRYPOINT ["runIPO.R"]  


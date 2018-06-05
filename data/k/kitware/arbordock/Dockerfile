FROM rocker/tidyverse:latest  
  
RUN apt-get update -qq && apt-get -y --no-install-recommends install \  
mesa-common-dev \  
libglu1-mesa-dev \  
libgsl0-dev \  
zlib1g-dev \  
libcurl4-openssl-dev \  
libmagick++-dev \  
libx11-dev  
  
RUN install2.r --error \  
\--deps TRUE \  
rgl \  
ape \  
geiger \  
nlme \  
diversitree \  
phytools  
  
RUN Rscript --slave --no-save --no-restore-history -e
"options(repos='http://cran.cnr.Berkeley.edu');library(devtools);install_github('arborworkflows/aRbor')"  
  
COPY run.R run.R  
COPY tasks.json tasks.json  
  
ENTRYPOINT ["Rscript", "run.R"]  


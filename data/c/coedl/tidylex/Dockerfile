FROM rocker/r-ver:3.4.3  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
libcurl4-openssl-dev \  
libssl-dev \  
libv8-dev \  
libxml2-dev \  
pandoc \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN Rscript -e 'install.packages("devtools")' \  
&& Rscript -e 'devtools::install_github("coedl/tidylex", dependencies =
c("Depends", "Imports", "Suggests"))'  
  
WORKDIR /  


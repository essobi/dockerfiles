FROM ubuntu:16.04  
MAINTAINER Milton Pividori <miltondp@gmail.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update && apt-get install -y --no-install-recommends \  
build-essential r-base libcairo2-dev libxt-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN R -e 'install.packages("EasyStrata", lib="/usr/local/lib/R/site-library",
repos = "https://cran.r-project.org")'  


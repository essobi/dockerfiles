FROM r-base:3.1.2  
MAINTAINER Alex Madrossan "madrossan@gmail.com"  
RUN apt-get update && apt-get install -y \  
curl \  
libcurl4-gnutls-dev \  
pandoc \  
pandoc-citeproc \  
texlive  
  
COPY init.* /  
RUN Rscript /init.R  
  
ENTRYPOINT ["/init.sh"]  


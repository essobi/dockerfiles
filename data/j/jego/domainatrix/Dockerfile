#################################################################  
# Dockerfile  
# Software: embassy-domainatrix  
# Software Version: 0.1.650-1  
# Description: The DOMAINATRIX programs were developed by Jon Ison and
colleagues at MRC HGMP for their protein domain research. They are included as
an EMBASSY package as a work in progress.  
# Website: http://emboss.sourceforge.net/what/  
# Tags: Proteomics|Genomics|General  
# Provides: embassy-domainatrix 0.1.650-1  
#################################################################  
  
# Base docker image  
FROM jego/emboss  
MAINTAINER test@armadillo.uqam.ca  
  
# Install embassy-domainatrix package  
RUN apt-get --quiet update \  
&& apt-get install -qqy \  
embassy-domainatrix=0.1.650-1 \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  


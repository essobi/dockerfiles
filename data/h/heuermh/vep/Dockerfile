FROM linuxbrew/linuxbrew  
MAINTAINER Michael Heuer <heuermh@acm.org>  
  
USER root  
RUN apt-get update && apt-get install -y \  
libarchive-zip-perl \  
libdbd-mysql-perl \  
libjson-perl  
  
USER linuxbrew  
RUN brew tap homebrew/science \  
&& brew install htslib \  
&& brew tap chapmanb/homebrew-cbl \  
&& brew install vep  


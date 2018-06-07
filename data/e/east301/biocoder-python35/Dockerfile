#  
# (c) 2016 biocoder developers  
#  
# This file is part of biocoder,  
# released under Apache License Version 2.0
(http://www.apache.org/licenses/LICENCE).  
#  
  
FROM python:3.5-slim  
MAINTAINER Shu Tadaka <tadaka@sb.ecei.tohoku.ac.jp>  
  
RUN apt-get update\  
&& apt-get install -y sudo time\  
&& apt-get autoremove -y\  
&& apt-get clean -y\  
&& rm -rf /var/lib/apt/lists/*\  
&& mkdir -p /biocoder/code /biocoder/input /biocoder/output /biocoder/system  


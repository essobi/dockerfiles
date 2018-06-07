#------------------------------------------------------------------------------  
# Copyright (c) 2015 The University of Manchester, UK.  
#  
# Licenced under LGPL version 2.1. See LICENCE for details.  
#  
# The IDInteraction Processing Pipelines were developed in the IDInteraction  
# project, funded by the Engineering and Physical Sciences Research Council,  
# UK through grant agreement number EP/M017133/1.  
#  
# Author: Robert Haines  
#------------------------------------------------------------------------------  
FROM idinteraction/base:2.0  
MAINTAINER Robert Haines <robert.haines@manchester.ac.uk>  
  
RUN apt-get update -q && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -qy \  
mencoder \  
\--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY resources/ $IDI_HOME  
  
ENTRYPOINT ["/usr/bin/make"]  
CMD ["all"]  


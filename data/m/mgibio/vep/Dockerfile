FROM ensemblorg/ensembl-vep:release_90.10  
MAINTAINER Susanna Kiwala <ssiebert@wustl.edu>  
  
LABEL \  
version="90" \  
description="VEP image with Wildtype and Downstream plugins"  
  
RUN mkdir -p /home/vep/Plugins  
WORKDIR /home/vep/Plugins  
RUN wget
https://raw.githubusercontent.com/Ensembl/VEP_plugins/release/90/Downstream.pm  
RUN wget
https://raw.githubusercontent.com/griffithlab/pVACtools/master/tools/pvacseq/VEP_plugins/Wildtype.pm  


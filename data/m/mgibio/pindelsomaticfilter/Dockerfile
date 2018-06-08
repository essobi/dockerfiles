FROM mgibio/pindel2vcf:0.6.3  
MAINTAINER Feiyu Du <fdu@wustl.edu>  
  
LABEL \  
version="v1" \  
description="pindel somatic filter"  
  
COPY somatic_indelfilter.pl /usr/bin/somatic_indelfilter.pl  
ENTRYPOINT ["/usr/bin/perl", "/usr/bin/somatic_indelfilter.pl"]  
  


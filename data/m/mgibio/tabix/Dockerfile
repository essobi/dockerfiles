FROM mgibio/samtools:1.3.1  
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>  
  
LABEL \  
version="1.3.1" \  
description="Tabix image for use in Workflows"  
  
RUN ln -s $SAMTOOLS_INSTALL_DIR/bin/tabix /usr/bin/tabix  
ENTRYPOINT ["/usr/bin/tabix"]  


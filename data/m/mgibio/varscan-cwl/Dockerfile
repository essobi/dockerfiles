FROM mgibio/samtools:1.3.1  
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>  
  
LABEL \  
version="v2.4.2-1.3.1" \  
description="Varscan+Samtools combined image for use in Workflows"  
  
RUN apt-get update && apt-get install -y \  
default-jre  
  
ENV VARSCAN_INSTALL_DIR=/opt/varscan  
  
WORKDIR $VARSCAN_INSTALL_DIR  
RUN wget
https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar
&& \  
ln -s VarScan.v2.4.2.jar VarScan.jar  
  
WORKDIR /  
ENTRYPOINT [] #clear the inherited entrypoint  
  
ADD cwl_helper.sh /usr/bin/  
CMD ["/usr/bin/cwl_helper.sh"]  


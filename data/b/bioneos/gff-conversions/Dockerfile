# Base image from Ubuntu #  
FROM ubuntu:17.10  
LABEL base.image="ubuntu:17.10"  
LABEL software="ea-utils"  
LABEL software.version="None"  
LABEL maintainer="Michael Lyon <malyon@bioneos.com>"  
  
USER root  
  
# Prep our container  
RUN apt-get update && apt-get install git python2.7 python-pip -y  
  
# Add gtf2bed, placed in /opt (using the static binary)  
RUN git clone https://github.com/ExpressionAnalysis/ea-utils.git /opt/ea-utils
&& cd /opt/ea-utils && git checkout bd148d4654fe26d8e218ef8f634fb6a6df9fede1  
  
# Clone the repository that contains gff3_to_bed_converter.py  
RUN git clone https://github.com/vipints/converters.git /opt/converters && cd
/opt/converters && git checkout c3e89918ef79e4b20498e56015f55281023a1043 &&
chmod +x /opt/converters/gfftools/codebase/gff3_to_bed_converter.py  
  
# Add our tools to the PATH  
ENV PATH /opt/ea-utils/clipper/:/opt/converters/gfftools/codebase/:$PATH  
  
# Default command  
CMD /bin/bash  


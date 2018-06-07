# Header  
FROM openjdk:8-jdk  
  
ENV CURRENT_VERSION "2.3.95"  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
unzip  
  
# Get the JNLP file  
ADD
http://data.broadinstitute.org/igv/projects/downloads/igvtools_$CURRENT_VERSION.zip
igvtools.zip  
  
# Unzip archive  
RUN unzip igvtools.zip -d /  
  
# Add alias of executable  
RUN echo 'alias igvtools="/IGVTools/igvtools"' >> ~/.bashrc  
RUN echo '#!/bin/bash igvtools' > /usr/bin/igvtools && \  
chmod +x /usr/bin/igvtools  


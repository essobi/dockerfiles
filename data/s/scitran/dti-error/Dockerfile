# Create Docker container that can run dtiError analysis.  
# Start with the Matlab r2015b runtime container  
FROM vistalab/mcr-v90  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install XVFB and other dependencies  
RUN apt-get update && apt-get install -y xvfb \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
unzip \  
wget  
  
# Install jq to parse the JSON config file  
RUN wget -N -qO- -O /usr/bin/jq
http://stedolan.github.io/jq/download/linux64/jq  
RUN chmod +x /usr/bin/jq  
  
# Set the diplay env variable for xvfb  
ENV DISPLAY :1.0  
# ADD the Matlab Stand-Alone (MSA) into the container.  
COPY src/bin/gear_dtiError /usr/local/bin/dtiError  
  
# Ensure that the executable files are executable  
RUN chmod +x /usr/local/bin/dtiError  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


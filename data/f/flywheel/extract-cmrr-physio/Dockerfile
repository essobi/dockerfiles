#Create Docker container that can extract CMRR physio data.  
# Start with the Matlab r2015b runtime container  
FROM flywheel/matlab-mcr:v90  
  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install XVFB and other dependencies  
RUN apt-get update && apt-get install -y \  
unzip \  
jq  
  
# ADD the Matlab Stand-Alone (MSA) into the container.  
COPY bin/extractCMRRPhysio_b81371d /usr/local/bin/extractCMRRPhysio  
  
# Ensure that the executable files are executable  
RUN chmod +x /usr/local/bin/extractCMRRPhysio  
  
# Directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
WORKDIR ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  
  


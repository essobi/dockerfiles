# Create Docker container that can run Gannet analyses.  
# Start with the Matlab r2015b runtime container  
FROM flywheel/matlab-mcr:v90  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y jq  
  
# ADD the Matlab Stand-Alone (MSA) into the container.  
ADD https://github.com/huawu02/Gannet_bin/raw/v3.0/GannetRun /bin  
ADD https://github.com/huawu02/Gannet_bin/raw/v3.0/run_Gannet.sh
/bin/run_Gannet  
  
# Ensure that the executable files are executable  
RUN chmod +x /bin/*  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


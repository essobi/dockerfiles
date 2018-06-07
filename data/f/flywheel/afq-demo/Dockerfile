# flywheel/afq-demo  
#  
FROM ubuntu:14.04  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y \  
zip  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Add demo data  
WORKDIR ${FLYWHEEL}  
COPY AFQ.zip ./AFQ.zip  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


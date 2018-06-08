# This Dockerfile constructs a docker image to run C-PAC  
#  
# Example build:  
# docker build --no-cache --tag flywheel/c-pac `pwd`  
#  
# Example usage: #TODO  
#  
# Start with the bids/cpac  
FROM bids/cpac:v1.0.1a_7  
  
# Note the Maintainer  
MAINTAINER Michael Perry <michaelperry@flywheel.io>  
  
# Install packages  
RUN apt-get update && apt-get install -y zip  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY bin/run \  
manifest.json \  
${FLYWHEEL}/  
  
# Handle file properties for execution  
RUN chmod +x ${FLYWHEEL}/run  
  
# Handle Environment preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD > ${FLYWHEEL}/docker-env.sh  
  
# Run the run.sh script on entry.  
ENTRYPOINT ["/flywheel/v0/run"]  


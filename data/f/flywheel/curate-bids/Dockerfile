# curate-bids  
FROM flywheel/bids-client:0.6.0  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install JQ to parse config file  
RUN apk add --no-cache jq  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


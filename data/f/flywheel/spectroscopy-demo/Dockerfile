# flywheel/spectroscopy-demo  
#  
FROM ubuntu:14.04  
MAINTAINER Ryan Sanford <ryansanford@flywheel.io>  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY manifest.json ${FLYWHEEL}  
  
# Run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY spectrum.csv ${FLYWHEEL}/spectrum.csv  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


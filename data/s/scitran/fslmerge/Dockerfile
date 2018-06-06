# Create a base docker container that will run fsl's fslmerge  
#  
FROM neurodebian:trusty  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Add sources  
RUN echo deb http://neurodeb.pirsquared.org data main contrib non-free >>
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN echo deb http://neurodeb.pirsquared.org trusty main contrib non-free >>
/etc/apt/sources.list.d/neurodebian.sources.list  
  
# Run apt-get calls  
RUN apt-get update \  
&& apt-get install -y \  
fsl-5.0-core \  
jq  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


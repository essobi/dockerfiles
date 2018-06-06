# flywheel/cortex-demo  
#  
FROM ubuntu:14.04  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
WORKDIR ${FLYWHEEL}  
ADD
https://storage.googleapis.com/flywheel/gears/data/demo_gears/cortex/metadata.json
./metadata.json  
  
# Add data from google storage  
WORKDIR ${FLYWHEEL}  
ADD
https://storage.googleapis.com/flywheel/gears/data/demo_gears/cortex/cortical_surface_right_hemisphere.obj
./cortical_surface_right_hemisphere.obj  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


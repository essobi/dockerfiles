# flywheel/ismrm-rd-demo  
#  
FROM ubuntu:14.04  
MAINTAINER Jennifer Reiter <jenniferreiter@invenshure.com>  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY manifest.json ${FLYWHEEL}  
  
# Copy run script  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
  
# Copy over output file  
COPY ismrmrd_raw.hdf5.tgz ${FLYWHEEL}/ismrmrd_raw.hdf5.tgz  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


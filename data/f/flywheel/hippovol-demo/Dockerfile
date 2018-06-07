# flywheel/hippovol-demo  
#  
FROM ubuntu:14.04  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY manifest.json ${FLYWHEEL}  
  
# Run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY hippocampus_seg_volume.csv ${FLYWHEEL}/hippocampus_seg_volume.csv  
COPY lh.asegHippo.nii.gz ${FLYWHEEL}/lh.asegHippo.nii.gz  
COPY rh.asegHippo.nii.gz ${FLYWHEEL}/rh.asegHippo.nii.gz  
COPY metadata.json ${FLYWHEEL}/metadata.json  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  
  


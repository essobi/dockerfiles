FROM miykael/nipype_advanced  
MAINTAINER Carlos Correa <cgc@stanford.edu>  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
WORKDIR ${FLYWHEEL}  
  
COPY run manifest.json align.csh run ${FLYWHEEL}/  
  
ENTRYPOINT ["/flywheel/v0/run"]  


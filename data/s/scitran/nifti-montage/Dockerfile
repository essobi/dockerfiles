# scitran/nifti-montage  
#  
# Use SciTran Data lib to generate a montage from a NIfTI file  
# See http://github.com/vistalab/data for source code.  
#  
FROM scitran/dcm-convert:v1.1.3  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
WORKDIR ${FLYWHEEL}  
  
# Put the code in place  
COPY run \  
manifest.json \  
nifti-montage.py \  
${FLYWHEEL}/  
  
run chmod +x nifti-montage.py  
run pip install --upgrade pillow  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


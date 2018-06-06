# scitran-apps/parrec-mr-classifier  
#  
# Use nibabel to classify raw PARREC data from Philips.  
#  
# Example usage:  
# docker run --rm -ti \  
# -v /path/to/dicom/data:/data \  
# scitran/parrec-mr-classifier \  
# /data/input.zip \  
# /data/outprefix  
#  
FROM ubuntu:trusty  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get -y install \  
python \  
python-pip \  
python-numpy \  
python-nibabel  
  
RUN pip install pytz  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Add code to determine measurement from acquisition label  
ADD
https://raw.githubusercontent.com/scitran/utilities/c438c7eb8ed8074c919e3ede8f295615023539ac/measurement_from_label.py
${FLYWHEEL}/measurement_from_label.py  
  
# Copy classifier code into place  
COPY parrec-mr-classifier.py ${FLYWHEEL}/parrec-mr-classifier.py  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


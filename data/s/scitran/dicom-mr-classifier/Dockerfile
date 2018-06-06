# scitran/dicom-mr-classifier  
#  
# Use pyDicom to classify raw DICOM data (zip) from Siemens, GE or Philips.  
#  
# Example usage:  
# docker run --rm -ti \  
# -v /path/to/dicom/data:/data \  
# scitran/dicom-mr-classifier \  
# /data/input.zip \  
# /data/outprefix  
#  
FROM ubuntu:trusty  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get -y install \  
python \  
python-dev \  
python-pip \  
jq  
  
# Install scitran.data dependencies  
RUN pip install \  
pydicom==0.9.9 \  
python-dateutil==2.6.0 \  
pytz==2017.2 \  
tzlocal==1.4 \  
nibabel==2.2.1  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Add code to determine classification from dicom descrip (label)  
COPY classification_from_label.py ${FLYWHEEL}/classification_from_label.py  
  
# Copy classifier code into place  
COPY dicom-mr-classifier.py ${FLYWHEEL}/dicom-mr-classifier.py  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


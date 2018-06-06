# scitran/dcm-convert  
#  
# Use SciTran Data lib to convert raw DICOM data (zip) from Siemens or GE to  
# various formats (montage, nifti, png).  
# See http://github.com/scitran/data for source code.  
#  
  
FROM ubuntu-debootstrap:trusty  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get -y install python-dev \  
python-virtualenv \  
git \  
libjpeg-dev \  
zlib1g-dev  
  
# Link libs: pillow jpegi and zlib support hack  
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib  
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib  
# Install scitran.data dependencies  
RUN pip install \  
numpy==1.9.0 \  
pytz \  
pillow \  
git+https://github.com/scitran/pydicom.git@0.9.9_value_vr_mismatch \  
git+https://github.com/nipy/nibabel.git@3bc31e9a6191fc54667b3387ed5dfaced46bf755
\  
git+https://github.com/moloney/dcmstack.git@6d49fe01235c08ae63c76fa2f3943b49c9b9832d
\  
git+https://github.com/scitran/data.git@bad266cbf7d284738bb8f426c7ca8ecc9de50bb5  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Put the code in place  
COPY run \  
manifest.json \  
dcm-convert.py \  
${FLYWHEEL}/  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


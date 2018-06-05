# Create Flywheel Gear for apply-canonical-xform  
#  
# FROM ubuntu:trusty  
FROM vistalab/mcr-v90  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install the MCR dependencies and some things we'll need and  
RUN apt-get -qq update && apt-get -qq install -y \  
unzip \  
zip \  
xorg \  
wget \  
python \  
curl  
  
# Download the MCR from Mathworks and silently install it  
# RUN mkdir /mcr-install && \  
# mkdir /opt/mcr && \  
# cd /mcr-install && \  
# wget
http://www.mathworks.com/supportfiles/downloads/R2015b/deployment_files/R2015b/installers/glnxa64/MCR_R2015b_glnxa64_installer.zip
&& \  
# cd /mcr-install && \  
# unzip -q MCR_R2015b_glnxa64_installer.zip && \  
# ./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \  
# cd / && \  
# rm -rf mcr-install  
#  
# # Configure environment variables for MCR  
# ENV LD_LIBRARY_PATH
/opt/mcr/v90/runtime/glnxa64:/opt/mcr/v90/bin/glnxa64:/opt/mcr/v90/sys/os/glnxa64  
# ENV XAPPLRESDIR /opt/mcr/v90/X11/app-defaults  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY bin/gear_niftiApplyCanonicalXform
${FLYWHEEL}/gear_niftiApplyCanonicalXform  
RUN chmod +x ${FLYWHEEL}/gear_niftiApplyCanonicalXform  
COPY bin/run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
ADD
https://raw.githubusercontent.com/scitran/utilities/daf5ebc7dac6dde1941ca2a6588cb6033750e38c/metadata_from_gear_output.py
${FLYWHEEL}/metadata_create.py  
RUN chmod +x ${FLYWHEEL}/metadata_create.py  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


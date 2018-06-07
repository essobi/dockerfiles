# Create Flywheel Gear that can run dtiInit  
# For source code see:  
#
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/dtiInit/standalone  
#  
# FROM ubuntu:trusty  
FROM flywheel/matlab-mcr:v82  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get -qq update && apt-get -qq install -y \  
unzip \  
xorg \  
wget \  
curl \  
zip \  
gzip \  
python  
  
# ADD the dtiInit Matlab Stand-Alone (MSA) into the container.  
ADD
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/dtiInit/standalone/executables/dtiInit_glnxa64_v82
/usr/local/bin/dtiInit  
  
# Add bet2 (FSL) to the container  
ADD https://github.com/vistalab/vistasoft/raw/97aa8a8/mrAnatomy/Segment/bet2
/usr/local/bin/  
  
# Add the MNI_EPI template and JSON schema files to the container  
ADD
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/templates/MNI_EPI.nii.gz
/templates/  
ADD
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/dtiInit/standalone/dtiInitStandAloneJsonSchema.json
/templates/  
  
# Copy the help text to display when no args are passed in.  
COPY source/doc/help.txt /opt/help.txt  
  
# Ensure that the executable files are executable  
RUN chmod +x /usr/local/bin/bet2 && chmod +x /usr/local/bin/dtiInit  
  
# Configure environment variables for bet2  
ENV FSLOUTPUTTYPE NIFTI_GZ  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure code  
COPY source/bin/run \  
source/bin/parse_config.py \  
manifest.json \  
${FLYWHEEL}/  
RUN chmod +x \  
${FLYWHEEL}/run \  
${FLYWHEEL}/parse_config.py  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


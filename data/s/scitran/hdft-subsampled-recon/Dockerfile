# scitran/hdft-subsampled-recon  
#  
# Create Flywheel compatible Gear that can run Sample Recon code from the
Schneider Lab,  
# University of Pittsburgh.  
#  
# Start with the Matlab r2016a runtime container  
FROM scitran/mcr-v901  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y \  
zip \  
gzip \  
python  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY bin/run \  
bin/run_subsampled_recon.sh \  
bin/subsampled_recon \  
bin/parse_config.py \  
manifest.json \  
${FLYWHEEL}/  
  
ADD
https://raw.githubusercontent.com/scitran/utilities/daf5ebc7dac6dde1941ca2a6588cb6033750e38c/metadata_from_gear_output.py
\  
${FLYWHEEL}/metadata_create.py  
  
# Handle file properties for execution  
RUN chmod +x \  
${FLYWHEEL}/run \  
${FLYWHEEL}/subsampled_recon \  
${FLYWHEEL}/run_subsampled_recon.sh \  
${FLYWHEEL}/parse_config.py \  
${FLYWHEEL}/metadata_create.py  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


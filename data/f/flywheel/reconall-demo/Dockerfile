# flywheel/reconall-demo  
#  
FROM ubuntu:14.04  
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
  
# Run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Add types from gitub  
WORKDIR ${FLYWHEEL}  
ADD
https://raw.githubusercontent.com/scitran/utilities/daf5ebc7dac6dde1941ca2a6588cb6033750e38c/metadata_from_gear_output.py
./metadata_create.py  
RUN chmod +x ${FLYWHEEL}/metadata_create.py  
  
# Add data from google storage  
WORKDIR ${FLYWHEEL}  
ADD demo_data.zip ./reconall.zip  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


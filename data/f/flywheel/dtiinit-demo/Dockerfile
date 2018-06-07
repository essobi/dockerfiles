# flywheel/dtiinit-demo  
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
COPY metadata_create.py ${FLYWHEEL}/metadata_create.py  
RUN chmod +x ${FLYWHEEL}/metadata_create.py  
  
# Add types from gitub  
WORKDIR ${FLYWHEEL}  
ADD
https://raw.githubusercontent.com/scitran/reaper/5e6d52565209fc2c35438c217aece9b235d58517/reaper/types.json
./types.json  
  
# Add data from google storage  
WORKDIR ${FLYWHEEL}  
ADD
https://storage.googleapis.com/flywheel/gears/data/demo_gears/dtiInit/DTI.zip
./DTI.zip  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


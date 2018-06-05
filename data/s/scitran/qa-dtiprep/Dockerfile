# Create a base docker container that will run dtiPrep  
#  
# Example usage:  
# docker run --rm -ti \  
# -v </path/to/input/data>:/flywheel/v0/input \  
# -v </path/to/output>:/flywheel/v0/output \  
# scitran/qa-dtiprep  
FROM vistalab/fsl-v5.0  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Run apt-get calls  
RUN apt-get update \  
&& apt-get install -y \  
mriconvert \  
python \  
libjpeg62 \  
tar  
  
# Install dtiPrep  
WORKDIR /opt  
ADD https://www.nitrc.org/frs/download.php/6630/DTIPrep1.2.4_linux64.tar.gz
dtiprep.tar.gz  
RUN tar -xf dtiprep.tar.gz && rm dtiprep.tar.gz  
  
# Configure environment (Must also be done in the run script)  
ENV PATH=$PATH:$/opt/DTIPrepPackage  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY qa-dtiprep.py ${FLYWHEEL}/qa-dtiprep.py  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Add metadata code  
WORKDIR ${FLYWHEEL}  
ADD
https://raw.githubusercontent.com/scitran/utilities/daf5ebc7dac6dde1941ca2a6588cb6033750e38c/metadata_from_gear_output.py
./metadata_create.py  
RUN chmod +x ${FLYWHEEL}/metadata_create.py ${FLYWHEEL}/qa-dtiprep.py
${FLYWHEEL}/run  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  
  


#flywheel/fmriprep  
  
############################  
# Get the fmriprep algorithm from DockerHub  
FROM poldracklab/fmriprep:1.0.15  
MAINTAINER Flywheel <support@flywheel.io>  
  
ENV FMRIPREP_VERSION 1.0.15  
  
############################  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
COPY parse_config.py /flywheel/v0/parse_config.py  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  
  
# Add the fmriprep dockerfile to the container  
ADD
https://raw.githubusercontent.com/poldracklab/fmriprep/${FMRIPREP_VERSION}/Dockerfile
${FLYWHEEL}/fmriprep_${FMRIPREP_VERSION}_Dockerfile  
  
  
############################  
# Install basic dependencies  
RUN apt-get update && apt-get -y install \  
jq \  
tar \  
zip \  
build-essential  
  
  
############################  
# Install the Flywheel SDK  
WORKDIR /opt/flywheel  
ENV COMMIT=d27f0a9  
RUN git clone https://github.com/flywheel-io/sdk workspace/src/flywheel.io/sdk  
RUN ln -s workspace/src/flywheel.io/sdk sdk  
RUN cd sdk && git checkout $COMMIT > /dev/null && cd ../  
RUN sdk/make.sh  
RUN sdk/bridge/make.sh  
ENV PYTHONPATH
/opt/flywheel/workspace/src/flywheel.io/sdk/bridge/dist/python/flywheel  
  
  
############################  
# Copy over python scripts that generate the BIDS hierarchy  
COPY create_archive.py /flywheel/v0/create_archive.py  
COPY create_archive_funcs.py /flywheel/v0/create_archive_funcs.py  
RUN chmod +x ${FLYWHEEL}/*  
  
  
############################  
# ENV preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD | \  
awk -F = '{ print "export " $1 "=\"" $2 "\"" }' > ${FLYWHEEL}/docker-env.sh  


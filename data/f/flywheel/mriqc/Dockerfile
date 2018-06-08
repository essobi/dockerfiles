#flywheel/mriqc  
# Get the MRIQC algorithm from DockerHub  
FROM poldracklab/mriqc:0.10.1  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install jq to parse the JSON config file  
RUN apt-get update && apt-get -y install jq zip  
  
# Install patched version of xvfbwrapper  
RUN pip install -q
https://github.com/ehlertjd/xvfbwrapper/releases/download/0.2.9.post1/xvfbwrapper-0.2.9.post1-py2.py3-none-
any.whl  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# ENV preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD | \  
awk -F = '{ print "export " $1 "=\"" $2 "\"" }' > ${FLYWHEEL}/docker-env.sh  
  
RUN echo "export XVFB_WRAPPER_SOFT_FILE_LOCK=1" >> ${FLYWHEEL}/docker-env.sh  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


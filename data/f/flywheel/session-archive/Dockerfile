# flywheel/session-archive  
FROM python:2.7  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install python package six  
RUN pip install six  
  
# Install Python SDK  
RUN pip install https://223-65499703-gh.circle-
artifacts.com/0/bridge/python/flywheel-0.0.1-py2-none-linux_x86_64.whl  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
COPY create_archive.py ${FLYWHEEL}/create_archive.py  
  
# ENV preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD | \  
awk -F = '{ print "export " $1 "=\"" $2 "\"" }' > /flywheel/v0/docker-env.sh  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]


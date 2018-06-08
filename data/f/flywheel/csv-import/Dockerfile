#flywheel/csv-import  
# Start with python 2.7  
FROM python:2.7  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install Python SDK  
RUN pip install https://github.com/flywheel-
io/sdk/releases/download/0.2.0/flywheel-0.2.0-py2-none-linux_x86_64.whl  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY script.py ${FLYWHEEL}/script.py  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# ENV preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD | \  
awk -F = '{ print "export " $1 "=\"" $2 "\"" }' > ${FLYWHEEL}/docker-env.sh  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  


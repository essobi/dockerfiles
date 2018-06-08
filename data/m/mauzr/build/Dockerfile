FROM python:3  
LABEL \  
org.label-schema.schema-version=1.0 \  
org.label-schema.name=mauzr/build:amd64 \  
org.label-schema.vcs-url=https://github.com/mauzr/build  
  
RUN pip3 install sphinx paho-mqtt pytest pytest-runner pytest-pylint \  
pyyaml wheel twine gitpython  
  
VOLUME /opt/mauzr  
WORKDIR /opt/mauzr  
ENTRYPOINT []  


# Base of your container  
FROM microsoft/aspnet:1.0.0-rc1-update1-coreclr  
  
MAINTAINER Stockport Digital By Design  
  
# Set an arg for the application we want to build (can be passed in /
overriden at build time)  
# See: https://docs.docker.com/engine/reference/builder/#arg  
ARG my_app=StockportContentApi  
ARG my_test=${my_app}Tests  
  
# Proxy ENV should be set in an env-file at runtime and passed in as build-
args at build-time  
# See: https://docs.docker.com/engine/reference/commandline/run/#set-
environment-variables-e-env-env-file  
# https://docs.docker.com/compose/env-file/  
# Create an app user to run containers as (running as root / uid is not a good
idea)  
# This may require a user of the same uid / gid if bind mounting to the host
filesystem  
ARG user=app  
ARG group=app  
ARG uid=2101  
ARG gid=2101  
RUN groupadd -g ${gid} ${group} \  
&& useradd -u ${uid} -g ${group} -m -s /bin/bash ${user}  
  
# Create an app folder to run the application in  
RUN mkdir -p /opt/app/src \  
&& mkdir -p /opt/app/test  
  
# Copy in files required for tests and nuget package "restore"  
# By not including all the code at this point the dnu restore will cache  
# and only run again on container build if we change the project.json files  
COPY global.json /opt/app/  
COPY src/${my_app}/project.json /opt/app/src/${my_app}/  
COPY test/${my_test}/project.json /opt/app/test/${my_test}/  
RUN chown -R ${user}:${group} /opt/app  
  
# Use app user for all further actions  
USER ${user}  
  
# Fetch nuget packages (restore?) in a cacheable way (one pass = one layer)  
# Running dnu restore in the test project pulls in all nuget deps picked up
from  
# project.json copied above. No need to run twice  
RUN cd /opt/app/src/${my_app} \  
&& dnu restore \  
&& cd /opt/app/test/${my_test} \  
&& dnu restore  
  
# Copy in code and tests  
COPY src/${my_app} /opt/app/src/${my_app}  
COPY test/${my_test} /opt/app/test/${my_test}  
  
# Lets test the code on build: tests fail, build fails  
WORKDIR /opt/app/test/${my_test}  
RUN dnx -p project.json test  
  
# Tests passed - we can continue the build  
# Expose the port that Kestrel listens on  
EXPOSE 5001  
# Start the application web target on running container  
WORKDIR /opt/app/src/${my_app}  
ENTRYPOINT [ "dnx", "-p", "project.json", "web" ]  


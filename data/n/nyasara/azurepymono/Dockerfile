FROM ubuntu:14.04  
# Install some basic system packages, and mono-devel so we get all the
libraries,  
# Create the /working folder for where code and programs will go  
# Make mono trust basic SSL  
RUN apt-get update && apt-get install -yq mono-devel curl git \  
&& mkdir /working \  
&& mozroots --import --ask-remove  
  
# Creates a working directory for later things to build on  
WORKDIR /working  
  
# Adds Azure SDK for Python  
COPY externals/azure-sdk-for-python/azure /working/azure  
  
# Adds IronPython  
COPY IronPython-2.7.4 /working/ipy  
  


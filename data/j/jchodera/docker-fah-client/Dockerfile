# Start with CUDA base image  
FROM kaixhin/cuda  
MAINTAINER John Chodera <john.chodera@choderalab.org>  
  
# Install curl and dependencies for FAH  
RUN apt-get update && apt-get install -y \  
wget  
  
# Retrieve fahclient and unpack it into /fah  
RUN mkdir fah && \  
cd fah && \  
wget https://fah.stanford.edu/file-releases/public/release/fahclient/debian-
testing-64bit/v7.4/fahclient_7.4.4_amd64.deb && \  
ar p fahclient_7.4.4_amd64.deb data.tar.gz | tar zx && \  
mv /fah/usr/bin/* /fah  
  
# Create a configuration file into the docker image.  
COPY config.xml /fah/config.xml  
  


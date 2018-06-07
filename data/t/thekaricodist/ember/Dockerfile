# =====================================================================  
# Commands  
#  
# Run the server  
# docker run --name ember -v $(pwd):/usr/src/app -P ember server  
#  
# =====================================================================  
# Base image  
FROM node:0.12.7  
# Setup commands, to install dependencies  
RUN npm install -g ember-cli@1.13.8  
  
# Ports to expose  
# These ports will be exposed, but unpublished by default  
#  
# You still have to specify `-P` on the command line  
# in order to _publish_ those ports to the "outside".  
#  
# The port that these will be mapped to is random. Check what  
# they are using the `docker ps` command  
EXPOSE 4200 49152  
# Directory to run commands in  
WORKDIR /usr/src/app  
  
# Binary to execute  
ENTRYPOINT ["/usr/local/bin/ember"]  
  
# Default parameters  
CMD ["help"]  


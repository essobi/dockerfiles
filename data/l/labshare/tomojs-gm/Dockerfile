# Base operating System  
FROM ubuntu:14.04  
  
# Start preparing environment  
# Suppress unnecessary warnings  
RUN export DEBIAN_FRONTEND=noninteractive  
  
# Update repositories  
RUN apt-get -y update && apt-get -y install graphicsmagick  
  
ENTRYPOINT ["gm"]


# docker image for building snaps  
#  
# Usage:  
#  
# from directory containing snapcraft.yaml  
# docker run -v $PWD:/app rocktchat/snapbuilder  
#  
# Note: build can take upwards of 10 minutes or more  
FROM ubuntu:16.04  
RUN groupadd -r snapuser \  
&& useradd -r -g snapuser snapuser  
  
RUN apt-get update && apt-get install -y \  
python \  
build-essential \  
snapcraft  
  
VOLUME /app  
  
WORKDIR /app  
  
CMD snapcraft stage && snapcraft snap  


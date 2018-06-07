# Thunderbird in a docker container  
#  
# Distributed under the MIT License, this is free software.  
# Do what you will with it  
#  
# Usage  
# docker run \  
# \--name thunderbird_"$(date +%s)" \  
# -d \  
# -v /path/to/thunderbird/config:/root/.thunderbird \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix"$DISPLAY" \  
# gruen/thunderbird  
FROM ubuntu:16.04  
MAINTAINER Darren Green <darren@gruen.site>  
RUN apt-get -y update \  
&& apt-get install -y thunderbird \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y  
CMD ["thunderbird"]  


FROM ozzyjohnson/cuda  
  
MAINTAINER Ozzy Johnson <docker@ozzy.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Versions.  
ENV BOINC_CLIENT 7.0.27+dfsg-5  
# Update and install minimal.  
RUN \  
apt-get update \  
\--quiet \  
&& apt-get install \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
boinc-client=${BOINC_CLIENT} \  
  
# Clean up packages.  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Data volume.  
ONBUILD VOLUME /data  
  
# Getting ready.  
WORKDIR /data  
  
# Default command.  
ENTRYPOINT ["/usr/bin/boinc"]  


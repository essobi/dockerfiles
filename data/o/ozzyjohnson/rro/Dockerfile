FROM debian:jessie  
  
MAINTAINER Ozzy Johnson <ozzy.johnson@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update and install minimal.  
RUN \  
apt-get update \  
\--quiet && \  
apt-get install \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
build-essential \  
gfortran \  
libcairo2 \  
libglib2.0-0 \  
libjpeg8 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libpng12-0 \  
libtiff5 \  
libx11-6 \  
libxt6 \  
liblzma-dev \  
wget && \  
# Clean up packages.  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Get RRO.  
RUN \  
wget \  
http://mran.revolutionanalytics.com/install/RRO-8.0-Beta-
Ubuntu-14.04.x86_64.tar.gz \  
-P /tmp && \  
tar -C /tmp -xzf /tmp/RRO-8.0-Beta-Ubuntu-14.04.x86_64.tar.gz && \  
dpkg -i /tmp/RRO-8.0-Beta-Ubuntu-14.04.x86_64.deb && \  
apt-get install \  
\--yes \  
-f && \  
rm /tmp/RRO-8.0-Beta-Ubuntu-14.04.x86_64.deb \  
/tmp/RRO-8.0-Beta-Ubuntu-14.04.x86_64.tar.gz \  
/tmp/install.sh && \  
  
# Clean up packages.  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Data volume.  
ONBUILD ["/data"]  
  
# Get ready to run.  
WORKDIR /data  
  
# Default command.  
ENTRYPOINT ["bash", "R"]  


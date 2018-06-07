# A basic debian image for graphical apps.  
# Contains X11 and QT5 libs.  
#  
# Build command:  
# docker build -t debian:graphical .  
  
FROM debian:jessie  
  
MAINTAINER Tom <info@webcore-it.com>  
  
# Make sure the repository information is up to date  
# and install all needed packages.  
RUN apt-get update && apt-get -y install \  
# basics  
ca-certificates \  
curl \  
tar \  
bzip2 \  
# gui libs  
libxss1 \  
libxslt1.1 \  
qt5-default \  
libgstreamer-plugins-base0.10-0 \  
libsqlite3-0 \  
  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*


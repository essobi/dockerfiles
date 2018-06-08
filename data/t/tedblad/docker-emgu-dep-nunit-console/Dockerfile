FROM mono:4.6  
  
############################  
### Install dependencies ###  
############################  
RUN apt-get -qq update \  
&& apt-get -y install build-essential monodevelop mono-mcs libtiff5-dev
libgeotiff-dev libgtk-3-dev libavcodec-dev libswscale-dev libavformat-dev
libopenexr-dev libjasper-dev libdc1394-22-dev libv4l-dev libeigen3-dev libtbb-
dev libtesseract-dev cmake-curses-gui ocl-icd-dev freeglut3-dev  
###############################  
### Install nunit-console ####  
###############################  
ARG VERSION_TAG=3.5  
ARG VERSION_NUMBER=3.5.0  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get -y install wget ca-certificates unzip \  
&& wget https://github.com/nunit/nunit-
console/releases/download/$VERSION_TAG/NUnit.Console-$VERSION_NUMBER.zip -O
/tmp/nunit.zip -nv \  
&& unzip -q /tmp/nunit.zip -d /opt/nunit-console/ \  
&& echo '#!/bin/sh\nmono /opt/nunit-console/nunit3-console.exe "$@"'
>/usr/local/bin/nunit3-console \  
&& chmod +x /usr/local/bin/nunit3-console \  
&& apt-get -y purge --auto-remove wget ca-certificates unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  


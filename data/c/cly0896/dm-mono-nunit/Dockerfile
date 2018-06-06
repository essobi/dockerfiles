FROM ubuntu:16.04  
MAINTAINER didstopia  
  
# Setup the locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Fixes apt-get warnings  
ENV DEBIAN_FRONTEND noninteractive  
ENV NUNIT_VERSION 3.8.0  
# Setup Mono repository  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list  
  
# Run a quick apt-get update/upgrade  
RUN apt-get update  
  
# Install dependencies  
RUN apt-get install -y \  
ca-certificates \  
software-properties-common \  
mono-complete \  
wget \  
git-core \  
curl  
  
RUN curl -o /usr/local/bin/nuget.exe
https://dist.nuget.org/win-x86-commandline/latest/nuget.exe  
  
RUN echo '#!/bin/bash\nmono /usr/local/bin/nuget.exe "$@"' > /usr/bin/nuget &&
\  
chmod +x /usr/bin/nuget  
  
RUN nuget install NUnit.ConsoleRunner -O /tmp/nunit -version $NUNIT_VERSION &&
\  
cp -r /tmp/nunit/NUnit.ConsoleRunner.$NUNIT_VERSION/tools/ /nunit/  
  
RUN echo '#!/bin/bash\nmono /nunit/nunit3-console.exe "$@"' > /usr/bin/nunit
&& \  
chmod +x /usr/bin/nunit  
# Cleanup  
ENV DEBIAN_FRONTEND newt  


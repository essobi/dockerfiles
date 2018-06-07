FROM microsoft/dotnet:2.0.4-sdk-2.1.3-jessie  
  
#  
# Install Mono:  
#  
ENV MONO_VERSION 5.0.0.100  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
official.list \  
&& apt-get update \  
&& apt-get install -y binutils mono-devel ca-certificates-mono fsharp mono-
vbnc nuget referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
#  
# Install docker client as described here  
# https://docs.docker.com/engine/installation/binaries/#install-static-
binaries  
#  
RUN apt-get update \  
&& apt-get install wget -y \  
&& apt-get install ca-certificates -y \  
&& cd /tmp \  
&& wget https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \  
&& tar zxvf docker-17.04.0-ce.tgz \  
&& cp -r docker/* /usr/bin/ \  
&& rm -r docker \  
&& rm docker*.tgz \  
&& rm -rf /var/lib/apt/lists/*  


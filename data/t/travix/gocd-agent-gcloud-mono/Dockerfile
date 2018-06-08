FROM travix/gocd-agent-gcloud:18.5.0  
  
MAINTAINER Travix  
  
ENV MONO_VERSION 5.2.0.215  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
official.list \  
&& apt-get update \  
&& apt-get install -y mono-runtime binutils curl mono-devel ca-certificates-
mono fsharp mono-vbnc nuget referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/* /tmp/*


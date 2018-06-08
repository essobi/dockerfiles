FROM debian:jessie  
  
MAINTAINER bt0r  
  
ENV MONO_VERSION 4.8  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
apache24-compat main" >> /etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" >> /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y binutils mono-devel ca-certificates-mono fsharp mono-
vbnc nuget referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
WORKDIR /home  


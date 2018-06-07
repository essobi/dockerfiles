FROM debian:wheezy  
  
MAINTAINER Emine Ben Tili <amine.bentili@gmail.com>  
  
#based on dockerfile by Jo Shields <jo.shields@xamarin.com>  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.2.1.102 main" > /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc
mono-4.0-service nuget \  
&& rm -rf /var/lib/apt/lists/*  


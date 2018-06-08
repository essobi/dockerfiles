FROM sunside/xenial-libuv:1.16.0  
MAINTAINER Markus Mayer <awesome@everybag.de>  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-wheezy.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y mono-runtime mono-mcs mono-xbuild mono-devel ca-
certificates-mono \  
fsharp msbuild nuget \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  


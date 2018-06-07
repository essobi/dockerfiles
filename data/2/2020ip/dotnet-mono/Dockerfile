FROM microsoft/dotnet  
MAINTAINER Jarrod Alexander <jarroda@2020research.com>  
  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get clean && apt-get update \  
&& apt-get install -y \--no-install-recommends \  
mono-devel \  
nuget \  
ca-certificates-mono


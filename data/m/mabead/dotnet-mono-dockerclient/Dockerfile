FROM microsoft/dotnet:1.0.5-sdk  
  
#  
# Install Mono:  
#  
# The recipe to install mono over the microsoft/dotnet image was taken from
here:  
# https://github.com/CL0SeY/dotnet-mono-docker/blob/master/1.0/sdk/Dockerfile  
#  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.4.2.11 main" | tee -a /etc/apt/sources.list.d/mono-
xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget
referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ln -s
/usr/share/dotnet/shared/Microsoft.NETCore.App/1.1.2/System.Native.so
/usr/lib/libSystem.Native.so  
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


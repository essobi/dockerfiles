#Pull base image  
FROM ubuntu:14.04  
# Run commands to modify the new image  
RUN apt-get update && apt-get install -y \  
git \  
mono-devel \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy snapshots
4.0.0" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list \  
  
#Nuget Configuration  
&& mozroots --sync --import \  
&& git clone https://github.com/Haacked/Nuget /tmp/nuget \  
&& /bin/bash -c 'cd /tmp/nuget ./build.sh' \  
&& cp /tmp/nuget/lib/NuGet.exe /usr/bin/NuGet.exe \  
&& sudo rm -r /tmp/nuget  


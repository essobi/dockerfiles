FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y curl sudo gendarme apt-transport-
https  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg && \  
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \  
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
ubuntu-trusty-prod trusty main" > /etc/apt/sources.list.d/dotnetdev.list'  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/ubuntu trusty main" | sudo tee
/etc/apt/sources.list.d/mono-official.list && \  
apt-get update && \  
apt-get install -y mono-devel ca-certificates-mono nunit-console  
  
#RUN mkdir -p /opt/paket && cd /opt/paket && \  
# curl -L https://github.com/fsprojects/Paket/archive/5.133.0.tar.gz -o
"paket.tar.gz" && \  
# tar -xvzf paket.tar.gz --strip 1 && \  
# rm paket.tar.gz  
#&& \  
# ./build.sh && \  
# ./install.sh  
  
RUN mkdir -p /opt/paket && cd /opt/paket && \  
curl -L
https://github.com/fsprojects/Paket/releases/download/5.133.0/paket.exe -o
"paket.exe" && \  
PAKET_SCRIPT='#!/bin/sh\nmono /opt/paket/paket.exe "$@"' && \  
echo $PAKET_SCRIPT > /usr/bin/paket && \  
chmod +x /usr/bin/paket  
  
RUN cd /opt/paket && \  
curl -L
https://github.com/wooga/Paket.Unity3D/releases/download/0.3.0/paket.unity3d.exe
-o "paket_unity3d.exe" && \  
PAKET3D_SCRIPT='#!/bin/sh\nmono /opt/paket/paket_unity3d.exe "$@"' && \  
echo $PAKET3D_SCRIPT > /usr/bin/paket_unity3d && \  
chmod +x /usr/bin/paket_unity3d  
  
RUN apt-get install -y git  
  
RUN cd ~ && git clone https://github.com/IvanRibakov/stylecopcli.git && cd
stylecopcli && git checkout path-fix && msbuild  
  
RUN mkdir /opt/nuget && \  
curl https://dist.nuget.org/win-x86-commandline/v4.4.1/nuget.exe -o
/opt/nuget/nuget.exe && \  
NUGET_SCRIPT='#!/bin/sh\nmono /opt/nuget/nuget.exe "$@"' && \  
echo $NUGET_SCRIPT > /usr/bin/nuget && \  
chmod +x /usr/bin/nuget  
  
RUN mkdir /opt/nunit && cd /opt/nunit && \  
nuget install NUnit && \  
nuget install NUnit.Runners && \  
NUNIT_SCRIPT='#!/bin/sh\nmono
/opt/nunit/NUnit.ConsoleRunner.3.8.0/tools/nunit3-console.exe "$@"' && \  
echo $NUNIT_SCRIPT > /usr/bin/nunit3-console && \  
chmod +x /usr/bin/nunit3-console  
  


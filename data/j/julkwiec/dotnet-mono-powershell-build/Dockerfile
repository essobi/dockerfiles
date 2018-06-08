FROM microsoft/dotnet:2-sdk-jessie  
  
SHELL ["/bin/bash", "-c"]  
  
# Install Mono, Powershell and F# compiler  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends apt-utils apt-transport-https \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add \- \  
&& sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-debian-jessie-prod jessie main"
> /etc/apt/sources.list.d/microsoft.list' \  
&& echo "deb http://download.mono-project.com/repo/debian alpha-jessie main" |
tee /etc/apt/sources.list.d/mono-official-alpha.list \  
&& apt-get update \  
&& apt-get install -y powershell binutils mono-devel referenceassemblies-pcl
ca-certificates ca-certificates-mono fsharp mono-vbnc nuget \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Preload Paket cache  
ENV PAKET_VERSION 5.114.0  
COPY paket.dependencies /tmp/warmup/  
RUN cd /tmp/warmup \  
&& curl -L -o ./paket.exe
"https://github.com/fsprojects/Paket/releases/download/$PAKET_VERSION/paket.exe"
\  
&& mono ./paket.exe install \  
&& cd / \  
&& rm -rf /tmp/warmup/  


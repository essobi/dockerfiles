FROM ubuntu:14.04  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
rm -rf /var/lib/apt/lists/* && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && apt-get -y upgrade && \  
apt-get install -y --no-install-recommends mono-devel ca-certificates-mono
nuget && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
CMD [ "mono" ]  


FROM slogsdon/develop-base  
  
ENV DOTNET_CORE_VERSION 1.0.0-rc2-3002702  
  
RUN \  
sudo apt-get update &&\  
sudo apt-get install -y --no-install-recommends \  
libicu52 \  
liblttng-ust0 \  
libunwind8 \  
&&\  
sudo rm -rf /var/lib/apt/lists/* &&\  
curl -SL
https://dotnetcli.blob.core.windows.net/dotnet/beta/Binaries/$DOTNET_CORE_VERSION/dotnet-
debian-x64.$DOTNET_CORE_VERSION.tar.gz --output dotnet.tar.gz &&\  
sudo mkdir -p /usr/share/dotnet &&\  
sudo tar -zxf dotnet.tar.gz -C /usr/share/dotnet &&\  
rm dotnet.tar.gz &&\  
sudo ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  


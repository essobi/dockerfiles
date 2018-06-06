FROM microsoft/mssql-server-linux:latest  
LABEL maintainer="Joe.Garcia@cyberark.com" \  
release-date="2018-01-10"  
  
RUN apt-get update && apt-get install -y curl \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | \  
apt-key add - \  
&& curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | \  
tee /etc/apt/sources.list.d/microsoft.list \  
&& apt-get update && apt-get install -y powershell \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pwsh -NoProfile -Command "Set-PSRepository -Name PSGallery
-InstallationPolicy Trusted; Install-Module PoShSkyTap"  
  
COPY . /etc/gsc  
  
WORKDIR /etc/gsc  
  
ENTRYPOINT pwsh -NoProfile -Command "./gsc.ps1"


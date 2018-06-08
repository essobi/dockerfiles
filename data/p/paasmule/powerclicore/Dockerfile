FROM microsoft/powershell:ubuntu16.04  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y unzip
&& apt-get clean  
  
RUN curl -L
https://github.com/mikefarah/yaml/releases/download/1.10/yaml_linux_amd64 -o
yaml && chmod +x yaml && mv yaml /usr/local/bin/yaml  
  
# Set working directory so stuff doesn't end up in /  
WORKDIR /root  
  
# Install VMware modules from PSGallery  
SHELL [ "pwsh", "-command" ]  
RUN Set-PSRepository -Name PSGallery -InstallationPolicy Trusted  
RUN Install-Module VMware.PowerCLI,PowerNSX  
  
# Add the PowerCLI Example Scripts and Modules  
# using ZIP instead of a git pull to save at least 100MB  
SHELL [ "bash", "-c"]  
RUN curl -o ./PowerCLI-Example-Scripts.zip -J -L
https://github.com/vmware/PowerCLI-Example-Scripts/archive/master.zip && \  
unzip PowerCLI-Example-Scripts.zip && \  
rm -f PowerCLI-Example-Scripts.zip && \  
mv ./PowerCLI-Example-Scripts-master ./PowerCLI-Example-Scripts && \  
mv ./PowerCLI-Example-Scripts/Modules/* /usr/local/share/powershell/Modules/  
  
CMD ["/usr/bin/pwsh"]  


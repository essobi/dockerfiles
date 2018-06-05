FROM microsoft/windowsservercore:latest  
  
MAINTAINER Alex Sarafian  
  
# C:\Repository will look like the current repository structure  
# C:\Repository\Publish is the publish folder. All scripts are aligned.  
ADD MiniNugetServer/ Repository/Source/MiniNugetServer  
COPY Start-Build.Docker.Run.ps1 Repository/Source/  
ADD https://github.com/Microsoft/iis-
docker/blob/master/windowsservercore/ServiceMonitor.exe?raw=true
/Repository/Publish/ServiceMonitor.exe  
  
# First empty line helps with commenting each line  
RUN powershell -NoProfile -NonInteractive -Command "\  
$ErrorPreference='Stop'; \  
Add-WindowsFeature Web-Server; \  
Add-WindowsFeature NET-Framework-45-ASPNET; \  
Add-WindowsFeature Web-Asp-Net45; \  
Remove-Item -Recurse C:\inetpub\wwwroot\\*; \  
"  
  
# First empty line helps with commenting each line  
RUN powershell -NoProfile -NonInteractive -Command "\  
$ErrorPreference='Stop'; \  
& C:\Repository\Source\Start-Build.Docker.Run.ps1 -InContainer; \  
& C:\Repository\Publish\New-Site.Docker.Run.ps1 -Port 80
-RemoveDefaultWebSite; \  
"  
  
# This instruction tells the container to listen on port 80.  
EXPOSE 80  
# set environment variables  
ENV apikey "mininugetserver"  
ENV packagesPath "~/Packages"  
CMD powershell -NoProfile -File "C:\Repository\Publish\Start-
ConfigurationServiceMonitor.Docker.Cmd.ps1" -ApiKey %apikey% -PackagesPath
%packagesPath%


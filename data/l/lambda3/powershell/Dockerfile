FROM ubuntu:16.04  
  
MAINTAINER Giovanni Bassi <giggio@giggio.net>  
RUN apt-get update \  
&& apt-get install apt-transport-https curl git vim libunwind8 libicu55 -y \  
&& sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 \  
&& apt-get update \  
&& apt-get install dotnet-dev-1.0.0-preview2-003121 -y  
RUN curl -SL
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-alpha.13/powershell_6.0.0-alpha.13-1ubuntu1.16.04.1_amd64.deb
\--output powershell.deb \  
&& dpkg --install powershell.deb \  
&& rm powershell.deb  
  
ENTRYPOINT ["powershell"]


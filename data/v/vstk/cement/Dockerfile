FROM skbkontur/cement:latest  
  
RUN apt-get update  
RUN apt-get --yes install curl apt-transport-https git  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-debian-jessie-prod jessie main"
> /etc/apt/sources.list.d/dotnetdev.list'  
  
RUN apt-get update  
RUN apt-get --yes install dotnet-sdk-2.0.0  
  
RUN curl https://raw.githubusercontent.com/vostok/cement-
modules/master/settings -L > ~/.cement/settings  


FROM wlniao/dotnet:deps2.0  
MAINTAINER WlniaoStudio <wlniao@qq.com>  
  
RUN apt-get update && apt-get install -y git vim && rm -rf
/var/lib/apt/lists/*  
RUN curl -SL
https://download.microsoft.com/download/D/7/2/D725E47F-A4F1-4285-8935-A91AE2FCC06A/dotnet-
sdk-2.0.3-linux-x64.tar.gz --output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet \  
&& mkdir /tmp/dotemp && cd /tmp/dotemp && dotnet new console && cd /wln && rm
-rf /tmp/dotemp  
  
ENTRYPOINT ["dotnet", "run"]  
ONBUILD COPY . /wln  
ONBUILD WORKDIR /wln  
ONBUILD RUN dotnet restore


FROM mono:4.6  
MAINTAINER Edijs Timosenko  
  
RUN mkdir -p /usr/src/app/source /usr/src/app/build  
WORKDIR /usr/src/app/source  
COPY . /usr/src/app/source  
RUN mono .nuget/NuGet.exe update -self  
RUN mono .nuget/NuGet.exe restore  
RUN xbuild /target:Migration_Migrator_Service /property:Configuration=Release
/property:OutDir=/usr/src/app/build/  
WORKDIR /usr/src/app/build  
  
ENTRYPOINT [ "mono", "./Migration.Migrator.Service.exe" ]


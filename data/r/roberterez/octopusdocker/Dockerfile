FROM microsoft/dotnet:2.1-runtime-alpine  
MAINTAINER someone someone@octopus.com  
  
#alpine doesnt have curl installed  
RUN apk add --no-cache curl  
  
ENV OCTO_TOOLS_VERSION 4.31.1  
ENV OCTO_TOOLS_DOWNLOAD_URL https://download.octopusdeploy.com/octopus-
tools/$OCTO_TOOLS_VERSION/OctopusTools.$OCTO_TOOLS_VERSION.portable.tar.gz  
  
WORKDIR /octo  
RUN curl ${OCTO_TOOLS_DOWNLOAD_URL} \--output OctopusTools.tar.gz && tar -zxvf
OctopusTools.tar.gz  
  
RUN apk del curl  
  
WORKDIR /src  
ENTRYPOINT ["dotnet", "/octo/Octo.dll"]  


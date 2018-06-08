# create source environment  
FROM microsoft/dotnet:2.1-sdk AS source  
WORKDIR /server  
  
# copy in the solution and restore  
COPY src/ .  
RUN dotnet restore  
  
# create a build environment from source  
FROM source AS build  
RUN dotnet build  
  
# take the build and publish the app  
FROM build AS publish  
WORKDIR /server/DemoCluster  
RUN dotnet publish -c RELEASE -o release  
  
# now create the runtime image  
FROM microsoft/dotnet:2.1-runtime AS runtime  
WORKDIR /server  
COPY \--from=publish /server/DemoCluster/release ./  
# default API port  
EXPOSE 5000  
# dashboard monitor port  
EXPOSE 8080  
# default silo to silo port  
EXPOSE 11111  
# default gateway port  
EXPOSE 30000  
ENTRYPOINT [ "dotnet", "DemoCluster.dll" ]


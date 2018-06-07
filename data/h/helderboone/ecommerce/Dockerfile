FROM microsoft/dotnet:2.1-sdk-alpine AS build-env  
WORKDIR /app  
  
COPY *.csproj ./  
RUN dotnet restore  
  
COPY . ./  
RUN dotnet publish -o out /p:PublishWithAspNetCoreTargetManifest="false"  
  
FROM microsoft/dotnet:2.1-runtime-alpine  
  
WORKDIR /app  
  
COPY \--from=build-env /app/out .  
  
ENTRYPOINT ["dotnet", "Ecommerce.dll"]  


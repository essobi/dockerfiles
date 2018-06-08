FROM microsoft/dotnet:2.1.300-rc1-sdk AS build-env  
WORKDIR /app  
  
# copy csproj and restore as distinct layers  
COPY *.csproj ./  
COPY NuGet.config ./  
RUN dotnet restore --configfile NuGet.config  
  
# copy everything else and build  
COPY . ./  
RUN dotnet publish -c Release -o out/  
  
# runtime env  
FROM microsoft/dotnet:2.1.300-rc1-sdk  
WORKDIR /app  
COPY \--from=build-env /app/out ./  
  
ENTRYPOINT ["dotnet", "OppaBot.dll", "/app/config.json"]


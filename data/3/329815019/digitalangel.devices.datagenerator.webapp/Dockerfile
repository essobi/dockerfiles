FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY
DigitalAngel.Devices.DataGenerator.WebApp/DigitalAngel.Devices.DataGenerator.WebApp.csproj
DigitalAngel.Devices.DataGenerator.WebApp/  
RUN dotnet restore
DigitalAngel.Devices.DataGenerator.WebApp/DigitalAngel.Devices.DataGenerator.WebApp.csproj  
COPY . .  
WORKDIR /src/DigitalAngel.Devices.DataGenerator.WebApp  
RUN dotnet build DigitalAngel.Devices.DataGenerator.WebApp.csproj -c Release
-o /app  
  
FROM build AS publish  
RUN dotnet publish DigitalAngel.Devices.DataGenerator.WebApp.csproj -c Release
-o /app -r linux-arm  
  
FROM microsoft/dotnet:2.0.0-runtime-stretch-arm32v7 AS final  
WORKDIR /app  
COPY \--from=publish /app .  
ENTRYPOINT ["dotnet", "DigitalAngel.Devices.DataGenerator.WebApp.dll"]  


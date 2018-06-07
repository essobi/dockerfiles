FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
#COPY *.sln ./  
COPY TestCF.csproj .  
RUN dotnet restore  
COPY . .  
WORKDIR /src/  
RUN dotnet build -c Release -o /app TestCF.csproj  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app TestCF.csproj  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
EXPOSE 80  
ENTRYPOINT ["dotnet", "TestCF.dll"]  


FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY Academia.sln ./  
COPY src/Academia.Web/Academia.Web.csproj src/Academia.Web/  
COPY src/Academia.Infrastructure/Academia.Infrastructure.csproj
src/Academia.Infrastructure/  
COPY src/Academia.Core/Academia.Core.csproj src/Academia.Core/  
RUN dotnet restore -nowarn:msb3202,nu1503  
COPY . .  
WORKDIR /src/src/Academia.Web  
RUN dotnet build -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
ENTRYPOINT ["dotnet", "Academia.Web.dll"]  


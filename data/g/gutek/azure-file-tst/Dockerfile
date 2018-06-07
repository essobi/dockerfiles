FROM microsoft/dotnet:2.0-runtime AS base  
WORKDIR /app  
  
FROM microsoft/dotnet:2.0-sdk AS build  
WORKDIR /src  
COPY ConsoleApp5.sln ./  
COPY ConsoleApp5/ConsoleApp5.csproj ConsoleApp5/  
RUN dotnet restore -nowarn:msb3202,nu1503  
COPY . .  
WORKDIR /src/ConsoleApp5  
RUN dotnet build ConsoleApp5.csproj -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish ConsoleApp5.csproj -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
ENTRYPOINT ["dotnet", "ConsoleApp5.dll"]  


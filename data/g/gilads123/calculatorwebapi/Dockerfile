FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY src/Calculator.WebApi/Calculator.WebApi.csproj src/Calculator.WebApi/  
COPY src/Calculator.Core/Calculator.Core.csproj src/Calculator.Core/  
RUN dotnet restore src/Calculator.WebApi/Calculator.WebApi.csproj  
COPY . .  
WORKDIR /src/src/Calculator.WebApi  
RUN dotnet build Calculator.WebApi.csproj -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish Calculator.WebApi.csproj -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
ENTRYPOINT ["dotnet", "Calculator.WebApi.dll"]  


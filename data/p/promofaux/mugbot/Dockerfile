FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
ENV ASPNETCORE_URLS=http://+:8080  
EXPOSE 8080  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
COPY *.sln ./  
COPY MugBot/MugBot.csproj MugBot/  
RUN dotnet restore  
COPY . .  
WORKDIR /src/MugBot  
RUN dotnet build -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
ENTRYPOINT ["dotnet", "MugBot.dll"]


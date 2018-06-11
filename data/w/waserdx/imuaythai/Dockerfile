FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
COPY . .  
CMD ASPNETCORE_URLS=http://*:$PORT dotnet IMuaythai.Api.dll  
  


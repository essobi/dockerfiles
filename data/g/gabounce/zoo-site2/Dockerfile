FROM microsoft/aspnetcore-build:2.0 as build-env  
WORKDIR /app  
  
COPY *.csproj ./  
RUN dotnet restore  
  
COPY . ./  
RUN dotnet publish -c release -o out  
  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
COPY \--from=build-env /app/out .  
ENTRYPOINT ["dotnet", "ZooSite2.dll"]


FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
COPY . /app  
WORKDIR /app  
RUN ["dotnet", "restore", "-s", "https://www.myget.org/F/easynetq-
unstable/api/v3/index.json", "-s", "https://api.nuget.org/v3/index.json"]  
  
ENTRYPOINT ["dotnet", "run"]  


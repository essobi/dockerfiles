  
FROM microsoft/aspnetcore:1  
LABEL Name=dotnet-webapp-test Version=0.0.0  
ARG source=.  
WORKDIR /app  
EXPOSE 5000  
COPY $source .  
ENTRYPOINT dotnet dotnet-webapp-test.dll  


  
FROM microsoft/aspnetcore:1  
LABEL Name=webapplication5 Version=0.0.1  
ARG source=.  
WORKDIR /app  
EXPOSE 3001  
COPY $source .  
ENTRYPOINT dotnet webapplication5.dll  


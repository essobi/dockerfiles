  
FROM microsoft/aspnetcore:1  
LABEL Name=helloworld Version=0.0.1  
ARG source=.  
WORKDIR /app  
EXPOSE 3000  
COPY $source .  
ENTRYPOINT dotnet helloworld.dll  


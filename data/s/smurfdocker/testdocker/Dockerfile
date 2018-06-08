FROM microsoft/dotnet:1.0.1-sdk-projectjson  
  
COPY . /app  
  
WORKDIR /app/src/TestDockerfile  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 80/tcp  
ENV ASPNETCORE_URLS http://*:80  
ENTRYPOINT ["dotnet", "run"]  
  


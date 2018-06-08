FROM microsoft/dotnet:latest  
  
ADD . /app  
  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5000"]  


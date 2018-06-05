FROM microsoft/dotnet:2.0-sdk  
WORKDIR /app/Api  
COPY . /app  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5000"]  


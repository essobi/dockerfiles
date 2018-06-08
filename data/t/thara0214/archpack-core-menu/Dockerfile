FROM microsoft/dotnet:1.0.1-sdk-projectjson  
  
COPY ./ /app  
  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
  
WORKDIR /app/src/MenuPrototype  
  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5000"]  


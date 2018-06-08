FROM microsoft/dotnet:1.1.0-sdk-projectjson  
  
COPY . /app  
  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 18204/tcp  
  
CMD ["dotnet", "run", "--server.urls", "http://*:18204"]  


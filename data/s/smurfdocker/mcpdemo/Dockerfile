FROM microsoft/dotnet:1.0.1-sdk-projectjson  
  
COPY . /app  
  
WORKDIR /app/src/McpDemo  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 5003/tcp  
ENV ASPNETCORE_URLS http://*:5003  
ENTRYPOINT ["dotnet", "run"]  
  


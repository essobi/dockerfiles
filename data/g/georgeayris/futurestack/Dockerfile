FROM microsoft/dotnet:1.0.1-sdk-projectjson  
COPY . /app  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build", "./src/FutureStack.Api"]  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
WORKDIR /app/src/FutureStack.Api  
ENTRYPOINT ["dotnet", "run"]  


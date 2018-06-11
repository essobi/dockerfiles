FROM microsoft/dotnet:latest  
COPY . /app  
WORKDIR /app  
  
RUN ["dotnet", "restore", "--source", "https://api.nuget.org/v3/index.json", "
--source", "https://www.myget.org/F/warden/api/v3/index.json", "--no-cache"]  
RUN ["dotnet", "build"]  
  
EXPOSE 5070/tcp  
ENV ASPNETCORE_URLS http://*:5070  
ENV ASPNETCORE_ENVIRONMENT production  
  
ENTRYPOINT ["dotnet", "run"]


FROM microsoft/dotnet  
COPY . ./app  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
  
ENV ASPNETCORE_URLS http://+:80  
ENTRYPOINT ["dotnet", "run"]  


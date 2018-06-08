FROM microsoft/aspnetcore-build:latest  
  
WORKDIR /app  
COPY . /app  
  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "publish", "-o", "/bin/dist", "-c", "release"]  
  
EXPOSE 80/tcp  
  
ENTRYPOINT ["dotnet", "/bin/dist/spd_cli.dll"]  


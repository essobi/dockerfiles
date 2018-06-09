FROM microsoft/aspnetcore:latest  
  
COPY out /app  
  
WORKDIR /app  
  
EXPOSE 5000  
ENTRYPOINT ["dotnet", "hook.dll"]  


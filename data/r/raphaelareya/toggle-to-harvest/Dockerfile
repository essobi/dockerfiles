FROM microsoft/dotnet:2.0.0-sdk-jessie  
  
WORKDIR app  
  
COPY . ./  
  
RUN dotnet restore  
RUN dotnet publish ./TogglMigrator.sln -c Release -o ./publish  
  
CMD ["dotnet", "./TogglMigrator/publish/TogglMigrator.dll"]  


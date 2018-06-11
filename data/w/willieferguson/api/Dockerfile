FROM microsoft/dotnet:1.0.1-runtime  
  
RUN mkdir -p /dotnetapp  
  
WORKDIR /dotnetapp  
COPY publish .  
  
ENTRYPOINT ["dotnet", "broker.dll"]  


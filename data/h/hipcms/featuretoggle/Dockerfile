FROM microsoft/dotnet:2.0.0-sdk-jessie  
  
RUN mkdir -p /dotnetapp  
  
COPY . /dotnetapp  
WORKDIR /dotnetapp/HiP-FeatureToggle  
  
EXPOSE 5000  
RUN (echo "131.234.137.23 tfs-hip.cs.upb.de" >> /etc/hosts) && dotnet build  
  
ENTRYPOINT ["dotnet", "run"]  


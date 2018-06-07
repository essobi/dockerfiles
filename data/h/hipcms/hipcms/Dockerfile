FROM microsoft/dotnet:1.1.1-sdk  
  
RUN mkdir -p /dotnetapp  
  
COPY src /dotnetapp  
WORKDIR /dotnetapp  
  
EXPOSE 5000  
VOLUME ["/dotnetapp/Api/wwwroot"]  
  
WORKDIR /dotnetapp/Api  
RUN dotnet restore --no-cache --configfile ./NuGet.Config  
ENTRYPOINT ["dotnet", "run"]  
  
#RUN dotnet publish -c Release -o out  
#ENTRYPOINT ["dotnet", "out/Api.dll"]  


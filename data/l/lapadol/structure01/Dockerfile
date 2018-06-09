FROM microsoft/aspnetcore-build:2.0.2-stretch AS publish  
  
ENV ASPNETCORE_URLS http://*:80  
ENV ASPNETCORE_ENVIRONMENT "Production"  
WORKDIR /src/  
COPY ./ .  
WORKDIR /src/Structure.Api/  
RUN dotnet restore  
RUN dotnet publish --output /src/Structure.Api/out  
  
FROM microsoft/aspnetcore-build:2.0.2-stretch  
  
ENV ASPNETCORE_URLS http://*:80  
ENV ASPNETCORE_ENVIRONMENT "Production"  
WORKDIR /dotnetapp  
COPY \--from=publish /src/Structure.Api/out .  
  
EXPOSE 80/tcp  
ENTRYPOINT ["dotnet", "Structure.Api.dll"]  


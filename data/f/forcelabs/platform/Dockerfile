FROM microsoft/dotnet:2.0-sdk  
  
MAINTAINER ForceLabs  
  
WORKDIR home  
  
RUN mkdir content-management-platform  
COPY . content-management-platform  
  
WORKDIR /home/content-management-platform/src/ForceLabs.Platform.Server  
  
RUN dotnet restore && dotnet build  
  
EXPOSE 5000  
ENTRYPOINT ["dotnet", "run", "0.0.0.0:5000"]  


FROM microsoft/aspnetcore:1.0  
ENTRYPOINT ["dotnet", "apis.dll"]  
ENV ASPNETCORE_ENVIRONMENT=production  
ARG source=./bin/Debug/netcoreapp1.0/publish  
WORKDIR /app  
EXPOSE 80  
COPY $source .  


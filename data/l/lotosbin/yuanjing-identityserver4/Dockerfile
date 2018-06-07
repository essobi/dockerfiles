FROM microsoft/aspnetcore:1.0  
ENTRYPOINT ["dotnet", "Host.dll"]  
ARG source=./bin/Debug/netcoreapp1.0/publish  
WORKDIR /app  
EXPOSE 80  
COPY $source .  


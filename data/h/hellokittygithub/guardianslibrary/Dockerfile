FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
  
# Copy everything else and build  
COPY . ./  
  
RUN chmod +x ./build.sh  
RUN ./build.sh  
  
# Build runtime image  
FROM microsoft/aspnetcore:2.0  
COPY \--from=build-env /app/src/Server/Guardians.Service.Authentication/out .  
ENTRYPOINT ["dotnet", "Guardians.Service.Authentication.dll
--usehttps=Certs/TLSCert.pfx --url=http://0.0.0.0:5001"]


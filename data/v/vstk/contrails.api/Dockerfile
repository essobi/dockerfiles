FROM vstk/cement:latest AS build-env  
WORKDIR /app  
COPY . ./  
RUN mono ../cement/dotnet/cm.exe update-deps  
RUN mono ../cement/dotnet/cm.exe build-deps -v  
RUN mono ../cement/dotnet/cm.exe build -v  
  
RUN dotnet publish -c Release -o out ./Vostok.Contrails.Api  
COPY ./Vostok.Contrails.Api/appsettings.json /app/appsettings.json  
  
# build runtime image  
FROM microsoft/aspnetcore:2.0-jessie  
  
WORKDIR /app  
COPY \--from=build-env /app ./  
  
ENTRYPOINT ["dotnet", "./Vostok.Contrails.Api/out/Vostok.Contrails.Api.dll"]  


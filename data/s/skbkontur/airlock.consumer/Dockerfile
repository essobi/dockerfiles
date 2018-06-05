FROM vstk/cement:latest AS build-env  
WORKDIR /app  
COPY . ./  
RUN mono ../cement/dotnet/cm.exe update-deps  
RUN mono ../cement/dotnet/cm.exe build-deps -v  
RUN mono ../cement/dotnet/cm.exe build -v  
RUN dotnet publish -c Release -o out  
  
# build runtime image  
FROM microsoft/dotnet:2.0-runtime-jessie  
  
WORKDIR /app  
COPY \--from=build-env /app ./  
COPY wait-for-it.sh /bin/wait-for-it.sh  
RUN chmod +x /bin/wait-for-it.sh  
  
ENTRYPOINT ["dotnet",
"/app/Vostok.Airlock.Consumer.Logs/out/Vostok.Airlock.Consumer.Logs.dll"]  
  


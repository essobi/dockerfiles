FROM microsoft/dotnet:2.0-sdk AS build-env  
WORKDIR /app  
  
# copy csproj and restore as distinct layers  
COPY *.csproj ./  
RUN dotnet restore  
  
# copy and build everything else  
COPY . ./  
RUN dotnet publish -c Release -o out  
  
# build runtime image  
FROM microsoft/dotnet:2.1-runtime  
WORKDIR /app  
COPY \--from=build-env /app/out ./  
ENTRYPOINT ["dotnet", "DrayTek WAN Status.dll"]  
  
VOLUME /app/config /app/data  
EXPOSE 51400/udp  


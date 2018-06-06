FROM microsoft/dotnet:2.0-sdk-jessie  
  
COPY . /build  
  
WORKDIR /build  
RUN dotnet restore  
RUN dotnet publish --configuration Release --output /build/out  
  
WORKDIR /build/out  
ENTRYPOINT ["dotnet", "/build/out/CfMes.dll"]


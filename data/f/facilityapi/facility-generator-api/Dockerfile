FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
WORKDIR /app  
COPY . /app  
  
RUN dotnet restore  
RUN dotnet publish src/Facility.GeneratorApi.WebApi -c Release -o out  
  
EXPOSE 45054  
ENTRYPOINT ["dotnet", "out/Facility.GeneratorApi.WebApi.dll"]  


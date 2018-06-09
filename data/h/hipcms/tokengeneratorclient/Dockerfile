FROM microsoft/dotnet:1.1.1-sdk  
  
RUN mkdir -p /dotnetapp  
COPY . /dotnetapp  
WORKDIR /dotnetapp  
  
EXPOSE 7017  
RUN dotnet restore  
  
ENTRYPOINT ["dotnet", "run"]  


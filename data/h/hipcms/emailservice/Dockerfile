FROM microsoft/dotnet:1.1-sdk  
  
RUN mkdir -p /dotnetapp  
  
COPY src /dotnetapp  
WORKDIR /dotnetapp  
  
EXPOSE 5002  
WORKDIR /dotnetapp/EmailService  
RUN dotnet restore  
ENTRYPOINT ["dotnet", "run"]


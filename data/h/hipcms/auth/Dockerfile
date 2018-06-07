FROM microsoft/dotnet:1.1.1-sdk  
  
#RUN dotnet nuget locals all --clear  
RUN mkdir -p /dotnetapp  
  
COPY src /dotnetapp  
WORKDIR /dotnetapp  
  
EXPOSE 5001  
WORKDIR /dotnetapp/Auth  
RUN dotnet restore --no-cache  
  
ENTRYPOINT ["dotnet", "run"]


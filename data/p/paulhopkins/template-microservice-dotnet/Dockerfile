FROM microsoft/dotnet:2-sdk  
  
WORKDIR /dotnetapp  
  
# copy and build everything else  
COPY dotnetapp.csproj /dotnetapp/  
COPY *.cs /dotnetapp/  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
  
ENTRYPOINT ["dotnet", "run"]  


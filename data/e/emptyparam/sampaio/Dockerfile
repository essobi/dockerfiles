FROM microsoft/dotnet:latest  
COPY . /app  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
RUN ["dotnet", "publish"]  
  
EXPOSE 5080/tcp  
  
ENV ASPNETCORE_URLS http://*5080  
ENV ASPNETCORE_ENVIRONMENT docker  
ENTRYPOINT ["dotnet", "Sampaio.dll", "--server.urls", "http://0.0.0.0:5080"]  


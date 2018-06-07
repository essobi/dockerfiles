FROM microsoft/dotnet:latest  
COPY . /app  
WORKDIR /app  
  
RUN ["dotnet", "restore", "--source", "https://api.nuget.org/v3/index.json", "
--no-cache"]  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
ENV ASPNETCORE_ENVIRONMENT development  
ENV LOCKBOX_SECRET_KEY j7ahgRF8fcYNgGwb4tEGLu4NYZTfD  
ENV LOCKBOX_MONGO_CONNECTION_STRING mongodb://mongo:27017  
ENV LOCKBOX_MONGO_DATABASE Lockbox  
  
ENTRYPOINT ["dotnet", "run"]  


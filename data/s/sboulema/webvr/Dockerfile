FROM microsoft/dotnet  
  
COPY . /dotnetapp  
WORKDIR /dotnetapp  
  
RUN dotnet restore  
  
EXPOSE 5000/tcp  
ENTRYPOINT dotnet run --server.urls http://0.0.0.0:5000


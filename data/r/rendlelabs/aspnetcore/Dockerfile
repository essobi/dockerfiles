FROM microsoft/dotnet:latest  
  
RUN apt-get update \  
&& apt-get install -y build-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /app  
  
COPY project.json .  
RUN dotnet restore && rm project.*  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT dotnet run --server.urls http://0.0.0.0:5000  


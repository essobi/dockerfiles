FROM microsoft/aspnet:latest  
  
COPY . /app  
WORKDIR /app  
  
RUN ["dnu", "restore"]  
  
ENTRYPOINT ["dnx","-p","project.json", "web"]  


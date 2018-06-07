FROM microsoft/aspnet:1.0.0-beta7-coreclr  
  
COPY ./AppAutomatedBuild/src/AppAutomatedBuild/ /app  
WORKDIR /app  
  
RUN ["dnu", "restore"]  
  
EXPOSE 5001  
ENTRYPOINT ["dnx", "kestrel"]


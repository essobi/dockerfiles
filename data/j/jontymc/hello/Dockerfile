FROM microsoft/dotnet:latest  
  
COPY project.json /app/  
WORKDIR /app  
RUN ["dotnet", "restore"]  
  
COPY . /app  
  
EXPOSE 5020/tcp  
ENV ASPNETCORE_URLS http://*:5020  
ENTRYPOINT ["dotnet", "run"]


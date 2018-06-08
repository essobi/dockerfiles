FROM microsoft/dotnet:latest  
COPY . /app  
WORKDIR /app/NerdCats.Auth  
  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build", "-c", "Release"]  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
ENTRYPOINT ["dotnet", "run", "-c", "Release"]


FROM microsoft/dotnet:latest  
COPY /release /app  
WORKDIR /app  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
ENTRYPOINT ["dotnet", "recipe.webapp.dll"]


FROM microsoft/dotnet:latest  
  
WORKDIR /app  
COPY . /app  
  
ENV ASPNETCORE_URLS http://+:80  
EXPOSE 80  
RUN dotnet restore  
  
ENTRYPOINT ["dotnet", "run"]  


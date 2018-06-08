FROM microsoft/dotnet:1.0.0-preview1  
  
WORKDIR /app  
COPY ["./project.json","/app"]  
RUN ["dotnet", "restore"]  
  
COPY . /app  
RUN ["dotnet","restore"]  
  
EXPOSE 5001/tcp  
  
ENTRYPOINT ["/app/docker/entrypoint.sh"]  
CMD ["dotnet", "run"]  


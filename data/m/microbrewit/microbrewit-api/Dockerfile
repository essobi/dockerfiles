FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
WORKDIR /app  
COPY ["./project.json","/app"]  
RUN ["dotnet", "restore"]  
  
COPY . /app  
RUN ["dotnet","restore"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["/app/docker/entrypoint.sh"]  
CMD ["dotnet", "run"]  


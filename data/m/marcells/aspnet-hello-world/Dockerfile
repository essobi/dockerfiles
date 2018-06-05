FROM microsoft/aspnet:1.0.0-beta4  
  
COPY ./data /app  
WORKDIR /app  
  
RUN ["dnu", "restore"]  
  
RUN apt-get install -y procps  
RUN chmod a+x /app/dnx_daemon  
  
EXPOSE 5004  
ENTRYPOINT ["/app/dnx_daemon", ".", "kestrel"]  


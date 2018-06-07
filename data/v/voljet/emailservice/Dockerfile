FROM microsoft/dotnet:latest  
COPY . /app  
WORKDIR /app  
  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
RUN chmod +x ./entrypoint.sh  
CMD /bin/bash ./entrypoint.sh


FROM microsoft/dotnet:1.0-sdk-projectjson  
  
COPY . /app  
  
WORKDIR /app  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN npm install -g angular-cli  
  
RUN cd broker-portal-demo-frontend && npm install && ng build --prod  
  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5000"]  


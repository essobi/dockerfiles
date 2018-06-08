FROM microsoft/dotnet:latest  
LABEL name "dockertest"  
  
RUN dotnet --info  
  
WORKDIR /app  
COPY src/ .  
  
WORKDIR /app/DockerTest  
RUN dotnet migrate && dotnet restore  
ENV ASPNETCORE_URLS http://*:5000  
EXPOSE 5000  
ENTRYPOINT dotnet run


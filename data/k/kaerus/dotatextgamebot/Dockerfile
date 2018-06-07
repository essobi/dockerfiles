FROM microsoft/dotnet:latest  
  
ARG source=bot  
WORKDIR /app  
COPY $source .  
  
RUN dotnet restore  
  
CMD ["/bin/bash", "-c", "dotnet run $TOKEN $CONNECTION"]


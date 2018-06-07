FROM microsoft/dotnet:latest  
WORKDIR /source  
COPY . .  
RUN dotnet restore  
RUN dotnet publish -c Release -o /app ./src/KidsPrize.Http  
EXPOSE 5000/tcp  
WORKDIR /app  
ENTRYPOINT dotnet KidsPrize.Http.dll


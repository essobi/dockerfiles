# Sample contents of Dockerfile  
# Stage 1  
FROM microsoft/aspnetcore-build AS builder  
WORKDIR /source  
  
# caches restore result by copying csproj file separately  
COPY *.csproj .  
RUN dotnet restore  
  
# copies the rest of your code  
COPY . .  
RUN dotnet publish --output /app/ --configuration Release  
  
# Stage 2  
FROM microsoft/aspnetcore  
WORKDIR /app  
COPY \--from=builder /app .  
ENV ASPNETCORE_URLS http://*:5000  
EXPOSE 5000  
ENTRYPOINT ["dotnet", "catnat-core.dll"]  


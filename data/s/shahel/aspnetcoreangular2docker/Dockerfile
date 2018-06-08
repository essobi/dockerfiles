FROM microsoft/aspnetcore-build  
WORKDIR /app  
  
COPY *.csproj .  
RUN dotnet restore  
  
COPY . .  
RUN dotnet publish /app/aspnetcoreangular2.csproj  


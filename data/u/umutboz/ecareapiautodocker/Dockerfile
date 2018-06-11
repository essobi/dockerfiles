FROM microsoft/dotnet:latest as builder  
COPY . /app  
WORKDIR /app  
  
run dotnet restore  
run dotnet build  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
ENV ASPNETCORE_ENVIRONMENT docker  
  
ENTRYPOINT dotnet run  
  
RUN dotnet build -c Release --no-restore  
  
RUN dotnet publish "EcareCore.csproj" -c Release -o "/dist" \--no-restore  
  
#Build the app image  
FROM microsoft/aspnetcore:2.0.3  
WORKDIR /app  
ENV ASPNETCORE_ENVIRONMENT Local  
ENTRYPOINT ["dotnet", "EcareCore.dll"]  
COPY \--from=builder /dist .  


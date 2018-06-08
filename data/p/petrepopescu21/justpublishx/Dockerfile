# Starting point  
FROM microsoft/aspnetcore-build:2.0 AS buildimage  
  
WORKDIR /app  
  
COPY *.csproj ./  
  
RUN dotnet restore  
  
COPY . ./  
  
RUN dotnet publish -c Release -o out  
  
# Run command  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
COPY \--from=buildimage /app/out .  
  
ENTRYPOINT ["dotnet","dockercore.dll"]


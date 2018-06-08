FROM microsoft/dotnet  
  
WORKDIR /app  
  
COPY *.csproj ./  
  
RUN dotnet restore  
  
COPY . ./  
  
RUN dotnet publish -c Release -o out  
  
ENTRYPOINT ["dotnet","out/my.dll"]


FROM microsoft/aspnetcore-build:2.0  
WORKDIR /app  
  
COPY *.csproj ./  
RUN dotnet restore  
  
COPY . ./  
RUN dotnet publish -c Release -o out  
  
EXPOSE 80  
ENTRYPOINT [ "dotnet","out/myweb.dll" ]  


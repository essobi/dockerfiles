FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
  
# Copy csproj and restore as distinct layers  
COPY . ./  
  
RUN dotnet restore  
RUN dotnet test test/DevkitApi.UnitTest/DevkitApi.UnitTest.csproj  
RUN dotnet test test/DevkitApi.IntTest/DevkitApi.IntTest.csproj  
  
# Copy everything else and build  
COPY . ./  
RUN dotnet publish src/DevkitApi.csproj -o out  
  
# Build runtime image  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
COPY \--from=build-env /app/src/out .  
EXPOSE 5000  
ENV ASPNETCORE_URLS http://*:5000  
ENTRYPOINT ["dotnet", "DevkitApi.dll"]


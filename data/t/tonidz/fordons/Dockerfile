# base image for ASP.NET Core  
FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
  
# Copy csproj and restore as distinct layers  
COPY *.csproj ./  
RUN dotnet restore  
  
# Copy everything else and build  
COPY . ./  
RUN npm rebuild node-sass --force  
RUN dotnet publish -c Release -o out  
  
# Build runtime image  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
COPY \--from=build-env /app/out .  
ENTRYPOINT ["dotnet", "vega.dll"]


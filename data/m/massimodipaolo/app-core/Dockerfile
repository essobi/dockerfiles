FROM microsoft/aspnetcore-build:latest AS build-env  
# Copy csproj and restore as distinct layers  
COPY . /app  
WORKDIR /app/samples/web  
RUN dotnet restore  
RUN dotnet publish -c Release -o out  
  
# App settings  
ENV ASPNETCORE_URLS http://*:5000  
EXPOSE 5000  
# Build runtime image  
FROM microsoft/aspnetcore:latest  
WORKDIR /app/samples/web  
COPY \--from=build-env /app/samples/web/out .  
ENTRYPOINT ["dotnet", "web.dll"]  


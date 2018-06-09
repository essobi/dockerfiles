#Set everything up  
FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
  
# Copy csproj and restore as distinct layers  
COPY *.csproj ./  
# COPY entrypoint.sh .  
RUN dotnet restore  
  
#Just copy the whole folder..  
COPY . .  
RUN dotnet publish -c Release -o out  
  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
EXPOSE 80  
COPY \--from=build-env /app/out .  
COPY entrypoint.sh .  
ENTRYPOINT ["sh", "entrypoint.sh"]


FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 80  
FROM microsoft/aspnetcore-build:2.0 AS build  
COPY . /src  
WORKDIR /src  
RUN dotnet restore && \  
dotnet build -c Release -o /app && \  
dotnet publish -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=build /app .  
ENTRYPOINT ["dotnet", "Blog.Website.dll"]  


FROM microsoft/aspnetcore:2.0 AS base  
WORKDIR /app  
EXPOSE 5000  
FROM microsoft/aspnetcore-build:2.0 AS build  
WORKDIR /src  
# Copy csproj and restore as distinct layers  
COPY *.csproj ./  
  
COPY . ./  
RUN dotnet restore  
  
RUN dotnet build -c Release -o /app  
  
FROM build AS publish  
RUN dotnet publish -c Release -o /app  
  
FROM base AS final  
WORKDIR /app  
COPY \--from=publish /app .  
RUN groupadd -g 1001 drrsnuser  
RUN useradd -r -u 1001 -g drrsnuser drrsnuser  
USER drrsnuser  
ENTRYPOINT ["dotnet", "AssessMETL.dll"]  


# build application  
FROM microsoft/aspnetcore-build:2.0 AS build-env  
WORKDIR /app  
  
COPY ./app/ ./  
  
RUN dotnet test tests \  
&& dotnet publish -c Release -o out  
  
# build runtime image  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
  
COPY \--from=build-env /app/web/out ./  
COPY scripts /usr/local/bin/  
  
ENV PING=http://localhost/api/health  
  
EXPOSE 80  
CMD ["dotnet", "web.dll"]  
  
HEALTHCHECK \--interval=30s --timeout=1s CMD run-health.sh || exit 1  


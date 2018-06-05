FROM microsoft/dotnet:2.0-runtime  
  
# Set ASP.NET Core environment variables  
ENV ASPNETCORE_ENVIRONMENT="Production"  
# Copy files to app directory  
COPY /release /app  
  
# Set working directory  
WORKDIR /app  
  
# Run  
ENTRYPOINT ["dotnet", "CachetMonitor.dll"]  


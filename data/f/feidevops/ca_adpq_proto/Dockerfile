FROM microsoft/aspnetcore:1.0  
# Set ASP.NET Core environment variables  
ENV ASPNETCORE_URLS="http://*:5000;https://*:5443"  
ENV ASPNETCORE_ENVIRONMENT="Production"  
# Copy files to app directory  
COPY /release /ca_proto  
  
# Set working directory  
WORKDIR /ca_proto  
  
# Open port  
EXPOSE 5000/tcp  
EXPOSE 5443/tcp  
  
# Run  
ENTRYPOINT ["dotnet", "ca_proto.dll"]


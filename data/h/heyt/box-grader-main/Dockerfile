FROM microsoft/aspnetcore:latest  
  
# Default Application TCP/Port.  
EXPOSE 80  
EXPOSE 9001  
EXPOSE 9011  
# Environment variables.  
ENV BGWEB_PORT=80  
# Application Volume.  
VOLUME [ "/app" ]  
  
# Set working dir.  
WORKDIR /app  
  
# Run Application.  
ENTRYPOINT ["dotnet", "BoxGraderWeb.dll"]  


FROM microsoft/aspnetcore:1.1  
WORKDIR /app  
EXPOSE 80  
ENV ASPNETCORE_URLS http://*:80  
COPY . /app  
ENTRYPOINT ["dotnet", "Presentation.Web.dll"]  


FROM microsoft/aspnetcore-build  
WORKDIR /app  
  
COPY AudiobookServer.WebApi ./AudiobookServer.WebApi/  
COPY AudiobookServer.Common ./AudiobookServer.Common/  
RUN ls  
WORKDIR /app/AudiobookServer.WebApi  
RUN dotnet restore  
RUN dotnet publish --output /out/ --configuration Release  
  
WORKDIR /out  
RUN rm -r /app  
EXPOSE 5001  
CMD ["dotnet", "AudiobookServer.WebApi.dll"]  


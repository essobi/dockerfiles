FROM microsoft/aspnetcore-build  
WORKDIR /app  
  
COPY AudiobookServer.CoreApi ./AudiobookServer.CoreApi/  
COPY AudiobookServer.Common ./AudiobookServer.Common/  
RUN ls  
WORKDIR /app/AudiobookServer.CoreApi  
RUN dotnet restore  
RUN dotnet publish --output /out/ --configuration Release  
  
WORKDIR /out  
RUN rm -r /app  
EXPOSE 5000  
CMD ["dotnet", "AudiobookServer.CoreApi.dll"]  


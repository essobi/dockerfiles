FROM microsoft/dotnet:runtime  
WORKDIR /dotnetapp  
  
# copy project.json and restore as distinct layers  
#COPY apis/project.json .  
#RUN dotnet restore  
# copy and build everything else  
#COPY apis/ .  
#RUN dotnet publish -c Release -o out  
COPY dist .  
ENTRYPOINT ["dotnet", "apis.dll"]  
EXPOSE 5000  


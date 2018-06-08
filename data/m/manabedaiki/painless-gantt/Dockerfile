FROM microsoft/dotnet:sdk AS build  
  
ADD ./ /source  
  
WORKDIR /source  
  
RUN dotnet publish --configuration=Release  
  
FROM microsoft/dotnet:runtime  
  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
COPY \--from=build /source/PainlessGanttCli/bin/Release/netcoreapp2.0/publish
/opt/PainlessGanttCli  
  
ENTRYPOINT ["dotnet", "/opt/PainlessGanttCli/PainlessGanttCli.dll"]  


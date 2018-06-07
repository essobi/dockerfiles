FROM microsoft/aspnetcore-build AS build  
  
WORKDIR /src/IconDiffBot  
COPY IconDiffBot/IconDiffBot.csproj .  
RUN dotnet restore  
  
COPY IconDiffBot/* ./  
RUN dotnet build -c Docker  
  
RUN dotnet publish -c Docker -o /app && cp entrypoint.sh /app/  
  
FROM microsoft/aspnetcore AS base  
  
EXPOSE 80  
#deps for System.Drawing  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libgdiplus \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /lib/x86_64-linux-gnu/libdl.so.2 /lib/x86_64-linux-gnu/libdl.so \  
&& mkdir /config_data  
  
WORKDIR /app  
COPY \--from=build /app .  
  
RUN mv appsettings.Docker.json /config_data/appsettings.Production.json  
VOLUME ["/config_data"]  
  
ENTRYPOINT ["./entrypoint.sh"]  


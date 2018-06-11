FROM microsoft/aspnetcore-build:1.0-1.1  
WORKDIR /app  
  
COPY . .  
RUN dotnet restore WetPicsTelegramBot.sln  
RUN dotnet publish WetPicsTelegramBot.sln -c Release -o out  
RUN find . -name \\* -print  
  
ENV ASPNETCORE_ENVIRONMENT Development  
  
ENTRYPOINT ["dotnet", "out/WetPicsTelegramBot.dll"]  


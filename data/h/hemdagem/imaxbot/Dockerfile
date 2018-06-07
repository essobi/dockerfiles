FROM microsoft/dotnet:1.1-sdk  
WORKDIR /app  
  
ENV SLACK_TOKEN=''  
ENV SLACK_BOT_NAME='imaxbot'  
COPY . ./  
RUN dotnet restore  
RUN dotnet publish -c Release -o out  
ENTRYPOINT ["dotnet", "/app/ImaxBot.Console/out/ImaxBot.Console.dll"]


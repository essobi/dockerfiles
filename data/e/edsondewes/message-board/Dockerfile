FROM microsoft/dotnet:2.1-sdk AS build-env  
WORKDIR /app  
  
# copy csproj and restore as distinct layers  
COPY *.sln .  
COPY MessageBoard.Messaging.Api/*.csproj ./MessageBoard.Messaging.Api/  
COPY MessageBoard.Messaging.Core/*.csproj ./MessageBoard.Messaging.Core/  
COPY MessageBoard.Messaging.Redis/*.csproj ./MessageBoard.Messaging.Redis/  
RUN dotnet restore  
  
# copy everything else and build  
COPY . ./  
WORKDIR /app/MessageBoard.Messaging.Api  
RUN dotnet publish -c Release -o out --no-restore  
  
# build runtime image  
FROM microsoft/dotnet:2.1-aspnetcore-runtime  
WORKDIR /app  
COPY \--from=build-env /app/MessageBoard.Messaging.Api/out ./  
  
HEALTHCHECK \--interval=2m --timeout=3s CMD curl --fail
http://localhost/health || exit 1  
ENTRYPOINT ["dotnet", "MessageBoard.Messaging.Api.dll"]


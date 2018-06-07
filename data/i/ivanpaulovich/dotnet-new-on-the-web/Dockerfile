FROM microsoft/dotnet:2.1-sdk  
COPY . .  
RUN dotnet new --install Paulovich.Caju  
WORKDIR /TaskRunnerApp.WorkerConsole  
RUN dotnet publish -o /app  
ENTRYPOINT ["dotnet", "/app/TaskRunnerApp.WorkerConsole.dll"]


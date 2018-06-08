#any other version throws sdk command error #dont miss the env name, it will
be used to form final container  
FROM microsoft/aspnetcore-build:2.0 as build-env  
ARG source  
  
WORKDIR /app  
  
# Copy csproj and restore as distinct layers  
COPY *.csproj ./  
RUN dotnet restore  
  
# Copy everything else and build  
COPY . ./  
RUN dotnet build  
  
RUN dotnet publish -c Release -o out  
  
FROM microsoft/aspnetcore:2.0  
WORKDIR /app  
  
EXPOSE 80  
#make sure obj/Docker/publish folder exists in side d project  
COPY \--from=build-env /app/out .  
  
ENTRYPOINT ["dotnet", "Wercker.TeamService.dll"]  


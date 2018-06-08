### STAGE 1: Build ###  
# We label our stage as 'builder'  
FROM microsoft/aspnetcore-build as builder  
  
# Change the workdir to the source dir  
WORKDIR /src  
  
# Copy the code to the docker image  
COPY /src .  
  
## Build the app and publish in app folder  
RUN dotnet publish --output /app/ --configuration Release  
  
### STAGE 2: Setup ###  
# This is the runtime image  
FROM microsoft/aspnetcore  
  
WORKDIR /app  
  
# Copy some required files  
# Copy build output file to use swagger  
COPY \--from=builder /src/main/bin/Debug/netcoreapp2.0/seed_dotnet.xml .  
  
# Copy database  
COPY \--from=builder /src/main/*.db .  
  
# Copy build output  
COPY \--from=builder /app .  
  
ENTRYPOINT ["dotnet", "main.dll"]


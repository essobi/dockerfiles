FROM microsoft/aspnetcore-build:2.0 AS build-env  
RUN mkdir /app  
WORKDIR /app  
  
# Copy csproj and restore as distinct layers  
COPY *.csproj ./  
RUN dotnet restore headhuntapi.csproj /p:StartupObject=headhuntapi.Program  
  
# Copy everything else and build  
COPY . ./  
  
RUN dotnet publish headhuntapi.csproj /p:StartupObject=headhuntapi.Program -o
/publish  
  
WORKDIR /publish  
  
ENTRYPOINT ["dotnet", "/publish/headhuntapi.dll",
"/p:StartupObject=headhuntapi.Program"]


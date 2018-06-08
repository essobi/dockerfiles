FROM microsoft/dotnet:2.0-sdk AS builder  
WORKDIR /app  
ADD /src/middleoffice.csproj /app  
RUN dotnet restore  
ADD /src /app  
RUN dotnet publish -o output  
FROM microsoft/aspnetcore:2.0  
COPY \--from=builder /app/output /app  
WORKDIR /app  
ENTRYPOINT ["dotnet", "middleoffice.dll"]


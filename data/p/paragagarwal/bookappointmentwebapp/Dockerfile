FROM microsoft/dotnet:2.0.3-sdk AS build-env  
WORKDIR /app  
  
copy . ./  
  
RUN dotnet restore  
  
WORKDIR /app/ElderlyBankingWebApp  
RUN dotnet publish -c Release -o out  
  
# build runtime image  
FROM microsoft/dotnet:2.0.3-runtime  
WORKDIR /app  
COPY \--from=build-env /app/ElderlyBankingWebApp/out ./  
  
EXPOSE 5000  
ENTRYPOINT ["dotnet", "ElderlyBankingWebApp.dll"]

